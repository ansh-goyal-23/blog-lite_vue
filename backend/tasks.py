
# from jobs.workers import celery
from scheduled_mails import *
from backend.models import User
from celery import Celery
# from flask import current_app as app
# app.app_context().push()
from datetime import datetime
# import celeryconfig
from celery.schedules import crontab

celery = Celery(broker = 'redis://localhost//', backend = 'redis://localhost')
celery.conf.beat_schedule = {
    # 'add-every-30-seconds': {
    #     'task': 'tasks.add',
    #     'schedule': 30.0,
    #     'args': (16, 20)
    # },
    'daily_mails': {
        'task': 'inactive_users',
        'schedule': crontab(hour=17, minute=30),
        'args': None
    },
    'monthly_mails': {
        'task': 'monthly_reports',
        'schedule': crontab(hour=1, minute=0, day_of_month=1),
        'args': None
    }

}
celery.conf.timezone = 'Asia/Kolkata'
celery.conf.update(
    result_expires=3600,
)

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='at every 10')

#     # # Calls test('world') every 30 seconds
#     # sender.add_periodic_task(30.0, test.s('world'), expires=10)

#     # DAILY REMINDER JOB AT 5:30 PM
#     sender.add_periodic_task(
#         crontab(hour='17', minute='30'),
#         test.s('Happy EVERYDAY!'),
#     )
#     # MONTHLY REMINDER JOB AT 1st OF EVERY MONTH
#     sender.add_periodic_task(
#         crontab(0, 0, day_of_month='1'),
#         test.s('Happy 1sts of Every Month!'),
#     )

# @celery.task
# def test(arg):
#     print(arg)

# @celery.task
# def add(x, y):
#     z = x + y
#     print(z)


@celery.task(name='tasks.send_daily_mails')
def send_daily_mails(user = {"name":"name", "email": "email"}):
    
    x = daily_post(data=user)
    return 200



def dates_diff(d1, d2):
    x = d1.strftime("%d/%m/%Y")
    x = x.split('/')
    y = d2.strftime("%d/%m/%Y")
    y = y.split('/')
    a = int(x[0]) + 30*int(x[1]) + 365*int(x[2])
    b = int(y[0]) + 30*int(y[1]) + 365*int(y[2])
    return a-b


@celery.task(name= "inactive_users")
def inactive_users():
    # from ...backend import app
    
    
    
    inact_users = []
    users = User.query.all()
    for user in users:
        post = user.posts[-1]
        recent_post_date = post.date_posted
        now = datetime.now()
        diff = dates_diff(now, recent_post_date)
        if diff >= 1:
            inact_users.append({"name": user.username, "email": user.email})

    print(inact_users)
    for user in inact_users:
        print(user)
        result = send_daily_mails.delay(user)
        # print(result.get(timeout=1, propagate=False))
    return result



@celery.task(name='tasks.send_monthly_mails')
def send_monthly_mails(dat = {"name":"name", "email" : "email", "posts_count": "0", "followers_count": "0", "following_count": "0"}):
    

    x = monthly_post(data=dat)
    return 200



@celery.task(name= "monthly_reports")
def monthly_reports():
    user_data = {"name":"name", "email" : "email", "posts_count": "0", "followers_count": "0", "following_count": "0"}
    
    users = User.query.all()
    for user in users:
        user_data["name"] = user.username
        user_data["email"] = user.email
        user_data["posts_count"] = len(user.posts)
        user_data["followers_count"] = len(user.followers) - 1
        user_data["following_count"] = len(user.followings) - 1
    
        result = send_monthly_mails.delay(user_data)
        # print(result.get(timeout=1, propagate=False))
    return result