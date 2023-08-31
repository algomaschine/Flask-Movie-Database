from typing import List
from project.models import UserFavorites

class FavoritesDao:
    def __init__(self, session) -> None:
        self.session = session

    def get_all(self, uid) -> List:
        """
        Returns all from user's favorites table by the user id.
        """
        return self.session.query(UserFavorites).filter(UserFavorites.user_id == uid).all()

    def add_movie_to_favorites(self, mid, user_id) -> None:
        """
        Adds the movie's id to the user's favorites in the database.
        """
        new_favorite = UserFavorites(user_id = user_id, movie_id = mid)
        self.session.add(new_favorite)
        self.session.commit()

    def delete_movie_from_favorites(self, mid, user_id) -> None:
        """
        Deletes the movie's id from the user's favorites in the database.
        """
        movie = self.get_one(mid, user_id)
        self.session.delete(movie)
        self.session.commit()

    def get_one(self, mid, uid) -> object:
        """
        Returns a movie from the user's favorites by movie's id from the database.
        """
        return self.session.query(UserFavorites).filter(UserFavorites.user_id == uid, UserFavorites.movie_id == mid).first()