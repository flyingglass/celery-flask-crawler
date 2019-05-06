import logging

from flask import request, jsonify
from flask_restplus import Namespace, Resource

from app.api.dto import UserDto
from app.api import api
from app.api.services import use_list_get, create_user, delete_user

ns = Namespace("user", description="User Restful API")

log = logging.getLogger(__name__)


@ns.route("/")
class UserApi(Resource):

    @api.marshal_list_with(UserDto.post_model)
    def get(self):
        """
        Returns list of user
        :return:
        """
        return use_list_get()

    @api.response(201, "User Successfully Created.")
    @api.expect(UserDto.post_model)
    def post(self):
        """
        Create User
        :return:
        """
        data = request.json
        create_user(data)
        return jsonify(msg="Success", code=201)

    @api.expect(UserDto.delete_model)
    @api.response(204, "User Successfully Deleted.")
    def delete(self):
        """
        Delete User
        :return:
        """
        args = UserDto.delete_model.parse_args(request)
        try:
            delete_user(args.get("user_id"))
            return jsonify(msg="Success", code=204)
        except Exception as e:
            log.exception(e)
            raise e
            # return jsonify(msg="Failed", code=500)
