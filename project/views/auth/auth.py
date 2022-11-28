from flask_restx import Namespace, Resource
from flask import request, abort
from project.container import users_service
from project.setup.api.models import user

api = Namespace('auth')
 
 
@api.route('/register/')
class AuthView(Resource):
    @api.marshal_with(user, code=201, description='OK')
    def post(self):
        """
        Register a new user.
        """
        data = request.json

        if data is None:
            abort(400, description='No data given')

        return users_service.create(data)
    

@api.route('/login/')
class AuthView(Resource):
    def post(self):
        """
        User login.
        """
        try:
            data = request.json
        except:
            abort(400, description='No data given')

        return users_service.login(data)


    def put(self):
        """
        Refresh access token for a logged in user.
        """
        data = request.json

        try:
            token = data['refresh_token']
        except:
            abort(401, description='Unauthorized')

        return users_service.approve_refresh_token(token)
