<i>Ридми на русском — ниже.</i>

# Flask movie database

<p><b>Technologies:</b> Flask, SQLAlchemy, SQLite, Docker.</p>

This is a Flask API for an online movie database with authentication and the CRUD for movies, directors, genres and users. The base structure of the API (like config factory, container, base DAO/service layers for base models, and overall module structure) was provided by the course tutors.

## How to run:
1. Copy the repository to your computer
2. Run the following commands in the terminal: <br>
`export FLASK_ENV=production` or `export FLASK_ENV=development`<br>
`export FLASK_APP=run.py` <br>
3. Run the create_tables.py file
4. Run the following command: <br>
`flask run`

## Main viewpoints

Swagger documentation is accessible on the root page (loacalhost:port/ where port is the port for the app you set up manually or the default port for the app) when the API is running in development mode.

## Challenges
<ul>
<p><li>When I was doing the project, it was not easy getting my head around the pre-maid part of it — its code was way ahead of the course curriculum. In the end, I understood it decently enough to integrate my own parts of code into it and also tweak some of the base code where needed.
After this project, the architecture of APIs built with Flask is one of my ongoing interests, since I've encountered the need to figure it out for my pet project Reminder.</li></p>

<p><li>The other difficulty was the structure of the project itself. Having to properly divide the API's logic into three layers and keep track of all of them was not easy. Eventually, I got used to it, but returning to this project after Django, I still find its structure to be complicated.</li></p>

<p><li>I have also encountered a problem with testing and auto-documenting the functions wrapped in the <i>@security.auth_required</i> decorator (the description for them was not visible in Swagger). For tests, I sought the help of a senior developer. He helped me write the tests for users' views. Considering the issue with Swagger documentation, I managed to solve it with the Flask-restx <i>@api.doc</i> decorator.</li></p>

<p><li>The most challenging part of the project was to automate the deployment of the API to the cloud server via Docker and GitHub actions, including the task of creating a Docker volume for the database.
The course info on Docker was scarce, so, to understand it better, I took a Docker mini-course. After that, I was able to create a working volume for a database.
Regarding deployment, I discovered the problem with containers built on M1 architecture. They would simply not run on the server. I solved this problem by building the images on the linux/amd64 platform. 
Also, My DevOps frriend helped me get confident with ssh connections and also toggle the server’s system settings so everything would run smoothly.</li></p>
</ul>

## Future enhancements
Currently, I am working on making a docker-compose file with a properly implemented NGINX for this project.

## Summary

This project is not perfect in any way. It was my first big project, so, once I have completed the main challenges, I decided to leave it as it is in order to continue learning and building new things.

<i>Here starts the Readme in Russian.</i>

# Курсовая работа по Flask: онлайн-база кино

<p><b>Технологии:</b> Flask, SQLAlchemy, SQLite, Docker.</p>

Это API на Flask для оналйн-базы кино с аутентификацией, CRUD для фильмов, режиссеров, жанров и пользователей. Базовая структура приложения (например, модуль с config factory, container, базовые DAO/service и модели) была предоставлена на курсе.

## Как запустить:
1. Скопируйте репозиторий на компьютер
2. В терминал введите следующие команды: <br>
`export FLASK_ENV=production` <br> или `export FLASK_ENV=development`
`export FLASK_APP=run.py` <br>
3. Запустите create_tables.py
4. В терминале введите: <br>
`flask run`

## Основные адреса

Подробный список адресов доступен в корне проекта (loacalhost:port/ port — заданный вами порт для приложения, либо порт приложения по умолчанию) во время работы API в режиме development.

## Трудности
<ul>
<p><li>Разобраться в структуре, которую дали для проекта, было непросто — код был гораздо сложнее того, что объясняли на курсе. Я разобралась достаточно для того, чтобы вписать свой код и даже править какие-то части изначального кода.
С тех пор архитектура приложений на Flask стала одной из самых интересных и насущных для меня тем (в том числе потому, что я столкнулась с необходимостью ее продумывать в своем пет-проекте Reminder).</li></p>

<p><li>Другой трудностью была сама структура проекта. Правильно разделить логику на три слоя, а еще держать в голове, что происходит на каждом из них, было непросто. Со временем я к этому привыкла, хотя после проектов на Django она все равно выглядит очень сложной.</li></p>

<p><li>Еще у меня возникла проблема с тестированием и автодокументацией функций, завернутых в декоратор <i>@security.auth_required</i>. Написать тесты мне помог коллега-сениор, а для документации я нашла решение в виде декоратора Flask-restx <i>@api.doc</i>.</li></p>

<p><li>Сложнее всего было автоматизировать развертку приложения на облачный сервер через Docker и GitHub actions, в том числе создать вольюм для базы данных. В программе курса материала по Docker было мало, поэтому, чтобы лучше разобраться, я прошла отдельный мини-курс по нему. После этого я смогла правильно настроить вольюм.
При развертке я столкнулась с тем, что контейнеры на архитектуре M1 на сервере просто не запускались. Решение, котороя я нашла — задавать платформу linux/amd64 для образов.
Мой друг-ДевОпс помог набраться понимания и уверенности с ssh-подключением, а также включить нужные системные настройки на сервере, чтобы все работало.</li></p>
</ul>

### Будущие улучшения

На данный момент я работаю над docker-compose с правильно подключенным NGINX для этого проекта.

## Дополнительно

Этот проект неидеален. Это было мой первый большой проект, поэтому, как только я закончила с основными задачами, я решила оставить его как есть, чтобы продолжить учиться новому и писать новый код.
