import logging

from flask import Blueprint
from flask_restplus import Api

# from .controller.user_api import ns as user_namespace
# from .controller.task_api import ns as task_namespace

log = logging.getLogger(__name__)

__all__ = ["blueprint", "api", "register_namespace"]

blueprint = Blueprint("api", __name__)
api = Api(
    blueprint,
    version="1.0",
    title="Flask Celery Crawler",
    description="Swagger API Doc"
)


def register_namespace():
    from .controller import user_namespace, task_namespace
    api.add_namespace(user_namespace, path="/user")
    api.add_namespace(task_namespace, path="/task")


@api.errorhandler
def default_error_handler(e):
    """Default error handler"""
    return {"msg": str(e)}, getattr(e, "code", 500)
