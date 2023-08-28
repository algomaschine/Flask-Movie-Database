from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = "movies"

    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    trailer = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    director_id = Column(Integer, ForeignKey('directors.id'))

    genre = relationship("Genre")
    director = relationship("Director")


class User(models.Base):
    __tablename__ = "users"

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favorite_genre = Column(Integer, ForeignKey('genres.id'))
    genre = relationship("Genre")


class UserFavorites(models.Base):
    __tablename__ = "userfavorites"

    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))

    user = relationship('User')
    movie = relationship('Movie')