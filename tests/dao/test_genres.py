import pytest
from project.dao import GenresDAO
from project.models import Genre


class TestGenresDAO:

    @pytest.fixture
    def genres_dao(self, db):
        return GenresDAO(db.session)

    @pytest.fixture
    def genre_1(self, db):
        g = Genre(name="Боевик")
        db.session.add(g)
        db.session.commit()
        return g

    @pytest.fixture
    def genre_2(self, db):
        g = Genre(name="Комедия")
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_genre_by_id(self, genre_1, genres_dao):
        """
        Checks if the function returns a correct genre object from the database.
        """
        assert genres_dao.get_by_id(genre_1.id) == genre_1

    def test_get_genre_by_id_not_found(self, genres_dao):
        """
        Checks if the function returns a 404 when the requested
        genre does not exist in the database.
        """
        assert not genres_dao.get_by_id(1)

    def test_get_all_genres(self, genres_dao, genre_1, genre_2):
        """
        Checks if the function returns a proper list of genre objects from the database.
        """
        assert genres_dao.get_all() == [genre_1, genre_2]

    def test_get_genres_by_page(self, app, genres_dao, genre_1, genre_2):
        """
        Checks if the pagination works correctly with a
        list of genre objects from the database.
        """
        app.config['ITEMS_PER_PAGE'] = 1
        assert genres_dao.get_all(page=1) == [genre_1]
        assert genres_dao.get_all(page=2) == [genre_2]
        assert genres_dao.get_all(page=3) == []
