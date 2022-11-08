from dao.model.user import UserSchema
from flask import request, abort
from flask_restx import Namespace, Resource

from decorators import auth_required
from implemented import user_service
from service.auth import get_email_from_header, check_password, change_the_password

# creating new namespace
user_ns = Namespace('/user')

# creating schemas for User
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        """
        returns data of certain user
        """
        req_header = request.headers['Authorization']

        email = get_email_from_header(req_header)

        if not email:
            abort(401)

        certain_user = user_service.get_by_email(email)

        return user_schema.dump(certain_user)

    @auth_required
    def patch(self):
        """
        updates name, surname and fav_gen of certain user
        """
        req_header = request.headers['Authorization']

        email = get_email_from_header(req_header)

        if not email:
            abort(401)

        req_data = request.json

        if not req_data:
            abort(401)

        req_data['email'] = email

        user_service.update(req_data)

        return '', 204


@user_ns.route('/password/')
class UserPasswordView(Resource):
    """
    updates password of certain user
    """
    @auth_required
    def put(self):
        password_1 = request.json.get('password_1')
        password_2 = request.json.get('password_2')
        header = request.headers['Authorization']
        email = get_email_from_header(header)

        return change_the_password(email, password_1, password_2)