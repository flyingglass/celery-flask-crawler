from flask_restplus import fields, reqparse

from app.api import api


class UserDto:
    post_model = api.model(
        "UserPostModel", {
            "id": fields.Integer(required=False),
            "username": fields.String(description="用户名，必传", required=True),
            "password": fields.String(description="密码，必传", required=True)
        }
    )

    delete_model = reqparse.RequestParser()
    delete_model.add_argument(
        "user_id", type=int, required=True, help="用户id"
    )
