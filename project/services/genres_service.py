from typing import Optional
from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Genre


class GenresService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genre:
        """
        Gets genre from the database.
        """
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f"Genre doesn't exist")

    def get_all(self, page: Optional[int] = None) -> list[Genre]:
        """
        Gets a list of all genres from the database.
        """
        return self.dao.get_all(page=page)
