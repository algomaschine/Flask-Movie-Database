from flask_restx import Namespace, Resource
from flask import abort
from project.container import genres_service
from project.setup.api.models import genre
from project.setup.api.parsers import page_parser

api = Namespace('genres')


@api.route('/')
class GenresView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(genre, as_list=True, code=200, description='OK')
    def get(self):
        """
        Gets a list of all genres.
        """
        return genres_service.get_all(**page_parser.parse_args())


@api.route('/<int:genre_id>/')
class GenreView(Resource):
    @api.marshal_with(genre, code=200, description='OK')
    def get(self, genre_id: int):
        """
        Gets genre by id.
        """
        return genres_service.get_item(genre_id)
            
