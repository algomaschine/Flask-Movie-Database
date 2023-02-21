from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao


    def get_item(self, pk: int) -> Movie:
        """
        Gets movie from the database.
        """
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')


    def get_all(self, page: Optional[int] = None) -> list[Movie]:
        """
        Gets a list of all movies from the database.
        """
        return self.dao.get_all(page=page)


    def get_all_new(self, page: Optional[int] = None) -> list[Movie]:
        """
        Gets a list of all movies from the database, ordered by
        the release year in a descending order.
        """
        return self.dao.get_all_new(page=page)