from flask import request, abort
from flask_restx import Namespace, Resource
from implemented import user_service
from service.auth import generate_tokens, approve_refresh_token

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class RegisterView(Resource):
    def post(self):
        """
        registers a new user
        """
        data = request.json

        user_service.create(data)

        return '', 201

@auth_ns.route('/login/')
class LoginView(Resource):
    def post(self):
        """
        generates access and refresh tokens
        """
        email = request.json.get('email')
        password = request.json.get('password')

        tokens = generate_tokens(email, password)

        return tokens, 201

    def put(self):
        """
        updates access and refresh tokens
        """
        refresh_token = request.json.get('refresh_token')

        tokens = approve_refresh_token(refresh_token)

        return tokens, 201