from flask_restx import Namespace, Resource
from flask import request, abort
from project.container import users_service
from project.setup.api.models import user
from project.tools import security

api = Namespace('auth')
 
 
@api.route('/register/')
class RegisterView(Resource):
    @api.marshal_with(user, code=201, description='OK')
    def post(self):
        """
        User register.
        """
        data = request.json
        if data is None:
            abort(400, description='No data given')
        return users_service.create(data)
    

@api.route('/login/')
class LoginView(Resource):
    def post(self):
        """
        User login.
        """
        data = request.json
        if data is None:
            abort(400, description='No data given')
        return users_service.login(data)

    def put(self):
        """
        Checks if the user's refresh token is valid and
        refreshes access token for a logged in user.
        """
        data = request.json
        try:
            token = data['refresh_token']
        except:
            abort(401, description='Unauthorized')
        return security._approve_refresh_token(token)
