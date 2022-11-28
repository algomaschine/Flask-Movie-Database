from project.models import UserFavorites

class FavoritesDao:
    def __init__(self, session):
        self.session = session

    def get_all(self, uid):
        return self.session.query(UserFavorites).filter(UserFavorites.user_id == uid).all()

    def add_movie_to_favorites(self, mid, user_id):
        new_favorite = UserFavorites(user_id = user_id, movie_id = mid)
        self.session.add(new_favorite)
        self.session.commit()
        return new_favorite.movie_id

    def delete_movie_from_favorites(self, mid, user_id):
        query = self.get_one(mid, user_id)
        self.session.delete(query)
        self.session.commit()
        return ""

    def get_one(self, mid, uid) -> bool:
        return self.session.query(UserFavorites).filter(UserFavorites.user_id == uid, UserFavorites.movie_id == mid).first()