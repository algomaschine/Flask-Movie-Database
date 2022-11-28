from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Квентин Тарантино'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Ла-Ла Ленд'),
    'description': fields.String(required=True, max_length=100, example='США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.'),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=lmB9VWm0okU'),
    'year': fields.Integer(required=True, example=2018),
    'rating': fields.Integer(required=True, example=6),
    'genre_id': fields.Integer(example=3),
    'director_id': fields.Integer(example=1)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='vasya@yandex.ru'),
    'name': fields.String(example='Vasya'),
    'surname': fields.String(example='Ivanov'),
    'favorite_genre': fields.Integer(example=3)
})

favorite_movie: Model = api.model('Любимые фильмы', {
    'movie_id': fields.Integer(required=True, example=1)
})