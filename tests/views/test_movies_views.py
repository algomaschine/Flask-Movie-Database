import pytest
from project.models import Movie


class TestMoviesView:
    @pytest.fixture
    def movie(self, db):
        obj = Movie(title="movie", description="description", trailer="trailer", year=1, rating=1)
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, movie):
        """
        Checks if the movies/ view returns a correct list
        of properly serialized movies objects.
        """
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.json == [{"id": movie.id, "title": movie.title, "description": movie.description, "trailer": movie.trailer, "year": movie.year, "rating": movie.rating, "genre_id": movie.genre_id, "director_id": movie.director_id}]

    def test_movie_pages(self, client, movie):
        """
        Checks if the movies view's pagination works correctly.
        """
        response = client.get("/movies/?page=1")
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/movies/?page=2")
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_movie(self, client, movie):
        """
        Checks if the movies/uid view returns a properly serialized movie object.
        """
        response = client.get("/movies/1/")
        assert response.status_code == 200
        assert response.json == {"id": movie.id, "title": movie.title, "description": movie.description, "trailer": movie.trailer, "year": movie.year, "rating": movie.rating, "genre_id": movie.genre_id, "director_id": movie.director_id}

    def test_movie_not_found(self, client, movie):
        """
        Checks if the movies/uid view returns a 404 when
        the requested movie does not exist in the database.
        """
        response = client.get("/movies/2/")
        assert response.status_code == 404
