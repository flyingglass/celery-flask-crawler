from flask_restplus import Namespace, Resource

from app.api.services import task_get

ns = Namespace("task", description="Task Restful API")


@ns.route("/")
class TaskApi(Resource):

    def get(self):
        """
        Execute Task
        :return:
        """
        task_get()
        return None, 200
