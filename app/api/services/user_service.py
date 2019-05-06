import logging

from sqlalchemy.orm.exc import NoResultFound

from app.database import db
from app.models import User
from app.tasks import *

log = logging.getLogger(__name__)


def use_list_get():
    # cron_task.delay(12, 13)
    # schedule_task.delay()
    # flask_scrapy("www.baidu.com")
    return User.query.all()


def create_user(model):
    username = model.get("username")
    password = model.get("password")

    db.session.add(User(username, password))
    db.session.commit()


def update_user(user_id, model):
    user = User.query.filter(User.id == user_id).one()
    user.username = model.get("username")
    db.session.add(user)
    db.session.commit()


def delete_user(user_id):
    try:
        user = User.query.filter(User.id == user_id).one()
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        raise e

