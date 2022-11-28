import pytest
from unittest.mock import patch

from project.models import User


class TestUserView:
    @pytest.fixture
    def user(self, db):
        obj = User(name="user", email="test", password="test")
        db.session.add(obj)
        db.session.commit()
        return obj

    @patch('jwt.decode')        
    def test_get_user(self, jwt_decode, user, client):

        response = client.get("/users/1", headers={'Authorization': "Bearer faketoken"})

        assert response.status_code == 200
        assert response.json == {"id": user.id, "name": user.name, "email": user.email, "surname": user.surname, "favorite_genre": user.favorite_genre}


    def test_user_not_found(self, client):
        response = client.get("/user/2")
        assert response.status_code == 404

