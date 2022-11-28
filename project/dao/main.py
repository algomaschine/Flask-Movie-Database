from project.dao.base import BaseDAO
from project.models import Genre, Movie, Director, User, UserFavorites


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre

class MoviesDAO(BaseDAO[Genre]):
    __model__ = Movie

class DirectorsDAO(BaseDAO[Genre]):
    __model__ = Director  

class UsersDAO(BaseDAO[Genre]):
    __model__ = User 

class UserFavoritesDAO(BaseDAO[Genre]):
    __model__ = UserFavorites 