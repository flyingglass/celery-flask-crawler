import logging
import time

from flask import current_app
from app import celery

log = logging.getLogger(__name__)


@celery.task(bind=True, ignore_result=True)
def schedule_task(self):
    app = current_app._get_current_object()

    log.info(app.config)
    log.info(self.request)
    # log.info("Request: {0!r}".format(self.request))


@celery.task(bind=True, ignore_result=True)
def cron_task(self, a, b):
    # app = current_app._get_current_object()
    #
    # log.info(app.config)
    # log.info(self.request)
    log.info("request:{}, a:{}, b:{}".format(self.request, a, b))
    log.info("fall sleep")
    time.sleep(5)
    log.info("wake up")