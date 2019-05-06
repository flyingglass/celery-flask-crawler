from app.tasks import flask_scrapy, cron_task, schedule_task


def task_get():
    cron_task.delay(12, 13)
    schedule_task.delay()
    flask_scrapy("www.baidu.com")