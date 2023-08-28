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

genres_dao = GenresDAO(db.session)
directors_dao = DirectorsDAO(db.session)
movies_dao = MoviesDAO(db.session)
users_dao = UsersDAO(db.session)
favorites_dao = FavoritesDao(db.session)

genres_service = GenresService(dao=genres_dao)
movies_service = MoviesService(dao=movies_dao)
directors_service = DirectorsService(dao=directors_dao)
users_service = UsersService(dao=users_dao)
favorites_service = FavoritesService(dao=favorites_dao)
