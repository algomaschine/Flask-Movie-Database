from flask_restx import Namespace, Resource
from flask import request, abort
from project.container import users_service
from project.setup.api.models import user
from project.tools import security
from project.exceptions import ItemNotFound, BadRequest

api = Namespace('users')


@api.route('/<int:uid>')
class UsersView(Resource):
    @api.marshal_with(user, code=200, description='OK')
    @api.doc(description='Gets user by id.')
    @security.auth_required
    def get(self, uid: int):
        """
        Gets user by id unless useer is not found.
        """
        return users_service.get_one_by_id(uid)

    @api.marshal_with(user, code=200, description='OK')
    @api.doc(description="Changes user's data.")
    @security.auth_required
    def patch(self, uid: int):
        """
        Changes user's data.
        """
        data = request.json
        if not data:
            raise BadRequest(f'No data given')
        return users_service.update(uid, data)

    @api.doc(description="Changes user's password.")
    @security.auth_required
    def put(self, uid: int):
        """
        Changes user's password.
        """
        data = request.json
        if not data:
            raise BadRequest(f'No data given')
        return users_service.update_password(uid=uid, data=data)