from typing import Optional
from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Director


class DirectorsService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Director:
        """
        Returns a director from the database by the id.
        """
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f"Director doesn't exist")

    def get_all(self, page: Optional[int] = None) -> list[Director]:
        """
        Returns a full list of directors from the database.
        """
        return self.dao.get_all(page=page)