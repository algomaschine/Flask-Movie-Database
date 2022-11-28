import jwt
from flask import abort

from project.dao.base import BaseDAO
from project.config import BaseConfig

config = BaseConfig()

class FavoritesService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_all(self, data):

        token = data.split('Bearer ')[-1]
        decoded_data = jwt.decode(token, key=config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])

        user_id = decoded_data["id"]
        
        return self.dao.get_all(user_id)

    def add_movie_to_favorites(self, mid, data):

        token = data.split('Bearer ')[-1]
        decoded_data = jwt.decode(token, key=config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])

        user_id = decoded_data["id"]

        if self.dao.get_one(mid, user_id):
            abort(400, description='Movie is already in your favorites')
        else:
            mid = self.dao.add_movie_to_favorites(mid, user_id)
            return 200

    def delete_movie_from_favorites(self, mid, data):
        token = data.split('Bearer ')[-1]
        decoded_data = jwt.decode(token, key=config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])

        user_id = decoded_data["id"]

        self.dao.delete_movie_from_favorites(mid, user_id)
        
        return 200
