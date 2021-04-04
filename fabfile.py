# -*- coding: utf-8 -*-
 
from fabric.api import *
from fabric.operations import local

 
env.hosts = ['178.128.152.77']
env.user  = 'root'

@task
def full_instalattion():
#     remote_info()
#     install_ubuntu_dependencies()
#     git_clone()
#     psql_conf()
#     pg_create_user()
#     pg_create_database()
#     permissions()
#     virtualenv_install()
    allow_ports()

def restart(command):
    return sudo('systemctl restart %s' % command)

def remote_info():
    run('uname -a')
 
def install_ubuntu_dependencies():
    sudo('apt-get update')
    sudo('apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx')
    sudo('pip3 install --upgrade pip')
    sudo('pip3 install virtualenv')

def git_clone():
    sudo('cd /home/ && git clone https://github.com/tr0v40/querosermb.git')
    sudo('chmod -R 755 /home/querosermb/')

def git_pull():
    sudo('cd /home/ && git pull')

def _run_as_pg(command):
    return sudo('sudo -u postgres %s' % command)

def pg_create_user(username='querosermb', password='password'):
    _run_as_pg('''psql -t -A -c "CREATE USER %(username)s WITH PASSWORD %(password)s;"''' % locals())

def pg_create_database(database='querosermb_db', owner='querosermb'):
    _run_as_pg('createdb %(database)s -O %(owner)s' % locals())

def permissions():
    _run_as_pg('''psql -t -A -c "GRANT ALL PRIVILEGES ON DATABASE querosermb_db TO querosermb"''')
#     _run_as_pg("GRANT ALL ON ALL TABLES IN SCHEMA public to querosermb;")
#     _run_as_pg("GRANT ALL ON ALL SEQUENCES IN SCHEMA public to querosermb;")
#     _run_as_pg("GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to querosermb;")

def virtualenv_install():
    sudo('virtualenv /home/querosermb/querosermb/_virtualenv')
    sudo(venv() +  'pip3 install -r /home/querosermb/requirements.txt')
    run(venv() +  'python manage.py migrate')

def venv():
    env = ('source /home/querosermb/querosermb/_virtualenv/bin/activate &&')
    return env

def allow_ports():
    sudo(venv() + 'ufw allow 8000')

def psql_conf():
    sudo('systemctl stop postgresql')
    sudo('cp /home/querosermb/meta/pg_hba.conf /etc/postgresql/12/main')
    sudo('systemctl start postgresql')

def gunicorn_config():
    sudo('systemctl start gunicorn')
    sudo('systemctl enable gunicorn')
