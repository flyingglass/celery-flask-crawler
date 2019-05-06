from __future__ import absolute_import
import logging.config
import os
import traceback

import yaml
from celery import Celery
from flask import Flask

from .config import config

log_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "logging.yml"))
with open(log_conf_path, "r") as f:
    logging.config.dictConfig(yaml.safe_load(f.read()))

log = logging.getLogger(__name__)

celery = Celery(
    __name__,
    backend=config.CELERY_RESULT_BACKEND,
    broker=config.CELERY_BROKER_URL,
    include=config.CELERY_INCLUDE
)


def make_celery(_app):
    celery.conf.update(
        CELERY_TIMEZONE=config.CELERY_TIMEZONE,
        CELERY_ENABLE_UTC=config.CELERY_ENABLE_UTC,
        CELERYD_LOG_FILE=config.CELERYD_LOG_FILE,
        CELERYBEAT_LOG_FILE=config.CELERYBEAT_LOG_FILE,
        CELERY_ACCEPT_CONTENT=config.CELERY_ACCEPT_CONTENT,
        CELERY_TASK_SERIALIZER=config.CELERY_TASK_SERIALIZER,
        CELERY_RESULT_SERIALIZER=config.CELERY_RESULT_SERIALIZER,
        CELERYBEAT_SCHEDULE=config.CELERYBEAT_SCHEDULE,
    )
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with _app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask


def create_app():
    _app = Flask(__name__)
    _app.config.from_object(config)

    make_celery(_app)
    # 需要先import然后再autodiscover_tasks
    # import app.tasks
    # celery.autodiscover_tasks(packages=config.CELERY_PACKAGES)

    from .database import db, redis_db, mongo_db
    redis_db.init_app(_app)
    mongo_db.init_app(_app)
    db.init_app(_app)

    from .api import blueprint as api_blueprint
    from .api import register_namespace
    register_namespace()
    _app.register_blueprint(api_blueprint, url_prefix="/api")

    log.info("App Ready...")
    log.info(_app.config)
    # log.info(traceback.extract_stack())

    return _app


app = create_app()
