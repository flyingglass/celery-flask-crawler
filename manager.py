import click
from app import app
from app.models import *

import logging

log = logging.getLogger(__name__)


# @click.command("hello")
@app.cli.command(
    help="command hello world"
)
@click.argument("name")
def hello(name):
    log.info(name)


@app.cli.command(
    name="create_all",
    help="创建所有的数据库表格"
)
def create_all():
    log.info("create_all")
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()


# app.cli.add_command(hello)
# app.cli.add_command(create_all)
