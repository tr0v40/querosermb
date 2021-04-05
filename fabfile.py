# -*- coding: utf-8 -*-
from fabric.api import task, run, cd, env, prefix, sudo, settings
from fabric.api import *

 
env.hosts = ['198.211.114.165']
env.user  = 'root'

@task
def full_instalattion():
    remote_info()
    install_ubuntu_dependencies()
    git_clone()
    psql_conf()
    pg_create_user()
    pg_create_database()
    # permissions()
    create_folder()
    virtualenv_install()
    populate()
    gunicorn_config()
    nginx_conf()
    restart_all()
    cron()

def restart(command):
    return sudo('systemctl restart %s' % command)

@task
def list_crons():
    run(venv() +  "Crontab(user='root')")

def remote_info():
    run('uname -a')
 
def install_ubuntu_dependencies():
    sudo('apt-get update')
    sudo('apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx cron')
    sudo('pip3 install --upgrade pip')
    sudo('pip3 install virtualenv')

def git_clone():
    sudo('cd /home/ && git clone https://github.com/tr0v40/querosermb.git')
    sudo('chmod -R 755 /home/querosermb/')

def git_pull():
    sudo('cd /home/ && git pull')

def create_folder():
    sudo('mkdir /home/querosermb/querosermb/static/')

def _run_as_pg(command):
    return run('sudo -u postgres %s' % command)

def pg_create_user():
    with settings(warn_only=True):
        run("sudo -su postgres createuser querosermb")

def pg_create_database():
    run('sudo -u postgres createdb querosermb_db --owner=querosermb')

def permissions():
    _run_as_pg('''psql -t -A -c "GRANT ALL PRIVILEGES ON DATABASE querosermb_db TO querosermb"''')

def venv():
    env = ('source /home/querosermb/querosermb/_virtualenv/bin/activate && ')
    return env

def virtualenv_install():
    sudo('virtualenv /home/querosermb/querosermb/_virtualenv')
    sudo(venv() +  'pip3 install -r /home/querosermb/requirements.txt')
    run(venv() +  'cd /home/querosermb/querosermb/ && python manage.py migrate')
    run(venv() +  'cd /home/querosermb/querosermb/ && python manage.py collectstatic')

def populate():
    run(venv() +  'cd /home/querosermb/querosermb/ && python populate.py')

def psql_conf():
    sudo('systemctl stop postgresql')
    sudo('cp /home/querosermb/meta/pg_hba.conf /etc/postgresql/12/main')
    sudo('systemctl start postgresql')

def gunicorn_config():
    sudo('cp /home/querosermb/meta/gunicorn.service /etc/systemd/system/')
    sudo('systemctl start gunicorn')
    sudo('systemctl enable gunicorn')
    sudo('systemctl daemon-reload')
    sudo('systemctl restart gunicorn')

def nginx_conf():
    sudo('cp /home/querosermb/meta/querosermb.conf /etc/nginx/sites-available/querosermb')
    sudo('ln -s /etc/nginx/sites-available/querosermb /etc/nginx/sites-enabled')
    sudo('systemctl restart nginx')
    sudo("ufw allow 'Nginx Full'")

def restart_all():
    sudo('systemctl daemon-reload')
    sudo('systemctl restart gunicorn')
    sudo('nginx -t')
    sudo('systemctl restart nginx')

def cron():
    execute('python /home/querosermb/cron.py')
    
