import logging
from multiprocessing import Process

from app import celery
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from scrapy_spiders.spiders.quotes import QuotesSpider

log = logging.getLogger(__name__)


@celery.task(bind=True, ignore_result=True)
def celery_scrapy(self, url):
    """
    在Celery中不可重复执行，太坑，直接废弃
    :param self:
    :param url:
    :return:
    """
    log.info(url)
    settings = Settings()
    process = CrawlerProcess(settings)
    process.crawl(QuotesSpider)
    process.start()


def _crawl():
    settings = Settings()
    crawler_process = CrawlerProcess(settings)
    crawler_process.crawl(QuotesSpider)
    crawler_process.start()


def flask_scrapy(url):
    log.info(url)

    p = Process(target=_crawl)
    p.start()
    p.join()
