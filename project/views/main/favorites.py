from flask import request
from flask_restx import Namespace, Resource
from project.container import favorites_service
from project.setup.api.models import favorite_movie
from project.tools import security
from project.exceptions import NotAuthorized

api = Namespace('favorites')


@api.route('/movies')
class FavoritesView(Resource):
    @api.marshal_with(favorite_movie, code=200, description='OK')
    @api.doc(description="Gets user's favorites.")
    @security.auth_required
    def get(self):
        """
        Gets user's favorites.
        """
        try:
            data = request.headers['Authorization']
        except:
            raise NotAuthorized(f'Not authorized')
        return favorites_service.get_all(data)


@api.route('/movies/<int:mid>')
class FavoriteView(Resource):
    @api.doc(description="Adds movie to user's favorites.")
    @security.auth_required
    def post(self, mid: int):
        """
        Adds movie to user's favorites.
        """
        try:
            data = request.headers['Authorization']
        except:
            raise NotAuthorized(f'Not authorized')
        return favorites_service.add_movie_to_favorites(mid, data)

    @api.doc(description="Deletes movie from user's favorites.")
    @security.auth_required
    def delete(self, mid: int):
        """
        Deletes movie from user's favorites.
        """
        try:
            data = request.headers['Authorization']
        except:
            raise NotAuthorized(f'Not authorized')
        return favorites_service.delete_movie_from_favorites(mid, data)