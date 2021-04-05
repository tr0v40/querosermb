from crontab import CronTab
 
def cron():
    my_cron = CronTab(user='root')
    job = my_cron.new(command='virtualenv /home/querosermb/querosermb/_virtualenv && cd /home/querosermb/querosermb/ && python manage.py incremental_request')
    job.minute.every(60)
    
    my_cron.write()