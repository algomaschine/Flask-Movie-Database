from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import favorites_service
from project.setup.api.models import favorite_movie
from project.tools import security

api = Namespace('favorites')

@api.route('/movies')
class FavoritesView(Resource):
    @api.marshal_with(favorite_movie, code=200, description='OK')
    @security.auth_required
    def get(self):
        """
        Get user favorites.
        """
        data = request.headers['Authorization']
        
        try:
            return favorites_service.get_all(data)
        except:
            abort(404, description='Favorites not found')


@api.route('/movies/<int:mid>')
class FavoriteView(Resource):
    @security.auth_required
    def post(self, mid):
        """
        Add movie to user favorites.
        """
        data = request.headers['Authorization']

        return favorites_service.add_movie_to_favorites(mid, data)


    @security.auth_required
    def delete(self, mid):
        """
        Delete movie from user favorites.
        """
        data = request.headers['Authorization']

        return favorites_service.delete_movie_from_favorites(mid, data)