from flask_restx import Namespace, Resource
from flask import request
from project.container import users_service
from project.setup.api.models import user
from project.tools import security
from project.exceptions import NotAuthorized, BadRequest

api = Namespace('auth')
 
 
@api.route('/register/')
class RegisterView(Resource):
    @api.marshal_with(user, code=201, description='OK')
    def post(self):
        """
        User register.
        """
        data = request.json
        if not data:
            raise BadRequest(f"Enter new user's data")
        return users_service.create(data)
    

@api.route('/login/')
class LoginView(Resource):
    def post(self):
        """
        User login.
        """
        data = request.json
        if not data:
            raise BadRequest(f"Enter the user's login and password")
        return users_service.login(data)

    def put(self):
        """
        Checks if the user's refresh token is valid and
        refreshes access token for a logged in user.
        """
        try:
            data = request.json
            token = data['refresh_token']
        except:
            raise NotAuthorized(f'Not authorized')
        return security._approve_refresh_token(token)
