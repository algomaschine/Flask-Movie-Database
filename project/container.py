from project.dao.main import GenresDAO
from project.dao.main import MoviesDAO
from project.dao.main import DirectorsDAO
from project.dao.users import UsersDAO
from project.dao.favorites import FavoritesDao


from project.services.genres_service import GenresService
from project.services.movies_service import MoviesService
from project.services.directors_service import DirectorsService
from project.services.users_service import UsersService
from project.services.favorites_service import FavoritesService

from project.setup.db import db
from project.tools import security

genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UsersDAO(db.session)
favorites_dao = FavoritesDao(db.session)

genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
director_service = DirectorsService(dao=director_dao)
users_service = UsersService(dao=user_dao)
favorites_service = FavoritesService(dao=favorites_dao)
