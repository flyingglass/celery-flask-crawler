import os

from datetime import timedelta

from celery.schedules import crontab


class BaseConfig(object):
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False

    def __getitem__(self, item):
        return self.__getattribute__(item)


class ProdConfig(BaseConfig):
    FLASK_DEBUG = False
    # CELERY
    CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
    CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
    CELERY_ACCEPT_CONTENT = ["application/json"]
    CELERY_TASK_SERIALIZER = "json"
    CELERY_RESULT_SERIALIZER = "json"
    CELERY_TIMEZONE = "Asia/Shanghai"


class DevConfig(BaseConfig):
    FLASK_DEBUG = True
    # CELERY
    CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
    CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
    CELERY_ACCEPT_CONTENT = ["application/json"]
    CELERY_TASK_SERIALIZER = "json"
    CELERY_RESULT_SERIALIZER = "json"
    CELERY_TIMEZONE = "Asia/Shanghai"
    CELERY_ENABLE_UTC = True
    CELERYD_LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "celery.log")
    CELERYBEAT_LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "beat.log")

    CELERY_INCLUDE = ["app.tasks"]
    # CELERY_PACKAGES = ["app.tasks"]

    CELERYBEAT_SCHEDULE = {
        "schedule_task": {
            "task": "app.tasks.celery.schedule_task",
            "schedule": timedelta(seconds=10)
        },
        "cron_task": {
            "task": "app.tasks.celery.cron_task",
            "schedule": crontab(minute="*"),
            "args": (3, 7)
        }
    }

    # Mongo, Redis, SQLAlchemy
    MONGO_URI = "mongodb://127.0.0.1:27017/crawler_db"
    REDIS_URL = "redis://127.0.0.1:6379/0"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root123@127.0.0.1:3306/test_db"
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://teamadmin:TAdm1n523@backend-web-db.cfpyyscjjkvu.us-east-1.rds' \
    #                           '.amazonaws.com:3306/test_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


mapping = {
    "dev": DevConfig,
    "prod": ProdConfig,

    "default": DevConfig
}

APP_ENV = os.environ.get("APP_ENV", "default").lower()
config = mapping[APP_ENV]()
