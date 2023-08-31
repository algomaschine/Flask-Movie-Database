import jwt
from flask import abort, Response
from typing import List
from project.dao.base import BaseDAO
from project.config import BaseConfig
from project.exceptions import NotAuthorized, ItemNotFound, BadRequest

config = BaseConfig()


class FavoritesService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_all(self, data) -> List:
        """
        Checks user's token and if success gets a full
        list of their favorite movies from the database.
        """
        try:
            token = data.split('Bearer ')[-1]
        except:
            raise NotAuthorized

        decoded_data = jwt.decode(token, key=config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
        user_id = decoded_data["id"]
        return self.dao.get_all(user_id)

    def add_movie_to_favorites(self, mid: int, data) -> None:
        """
        Checks user's token, if success checks if a movie
        is already in user's favorites. If not, ads a
        movie to the list of user's favorites.
        It has a bug I haven't been able to fix
        yet — it allows to add the movie that doesn't
        exist.
        """
        try:
            token = data.split('Bearer ')[-1]
        except:
            raise NotAuthorized

        decoded_data = jwt.decode(token, key=config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
        user_id = decoded_data["id"]

        if self.dao.get_one(mid, user_id):
            raise BadRequest(f'Movie is already in your favorites')
        else:
            self.dao.add_movie_to_favorites(mid, user_id)
            return Response('OK', status=200)

    def delete_movie_from_favorites(self, mid: int, data) -> None:
        """
        Checks user's token and if success deletes a movie
        from their list of favorites.
        """
        try:
            token = data.split('Bearer ')[-1]
        except:
            raise NotAuthorized

        decoded_data = jwt.decode(token, key=config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
        user_id = decoded_data["id"]
        
        try:
            self.dao.delete_movie_from_favorites(mid, user_id)
        except:
            raise ItemNotFound(f"Movie doesn't exist")
            
        return Response('OK', status=200)
