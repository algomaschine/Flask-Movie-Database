<i>Промотайте вниз, чтобы прочитать ридми на русском.</i>

# Flask coursework

<p><b>Technologies:</b> Flask, PostgresQL, SQLAlchemy, Docker, SQLite.</p>

This is a web app written with Flask framework. It imitates an online movie database with a CRUD for movies, directors, genres and users, authentication, and a possibility for users to add movies to their favorites. The bone structure of the app (like config factory, container, base DAO/service layers for base models, and overall module structure) was provided by the course tutors.

## How to run:
1. Copy the repository to your computer
2. Run the following commands in the terminal: <br>
`export FLASK_ENV=production` <br>
`export FLASK_APP=run.py` <br>
3. Run the create_tables.py file
4. Run the following command: <br>
`flask run`

## Challenges
<ul>
<p><li>Getting my head around the pre-maid part of the project was not easy — its code was way ahead of the code I was taught on the course at that time. I deciphered the pre-established parts of code decently enough to use them and integrate my own parts of code into it. After that, the architecture of apps built with Flask is one of my ongoing interests, since I've encountered the need to figure it out for my pet-project Reminder and haven't found a solution that would have satisfied me yet.</li></p>

<p><li>The other difficulty was the structure of the project itself. Having to correctly divide the app logic into three layers and keep track of all of them was not easy. Eventually, I got used to it, but returning to this project after Django, I still find its structure to be very complicated.</li></p>

<p><li>I have also encountered a problem with testing and auto-documenting functions wrapped in the <i>@security.auth_required</i> decorator with Swagger. For testing functions, I sought the help of a senior developer. He helped me to write the tests for users' views. With Swagger, I came up with a fix of Flask-restx <i>@api.doc</i> decorator.</li></p>

<p><li>The most challenging part was to automate the deployment of the app to the cloud server via Docker and GitHub actions, including the task of creating a Docker volume for the database.
The course info on Docker was scarce, so, to understand it better, I took a Docker mini-course. It helped me create a well-functioning volume for a database.
Regarding deployment, I had to discover the problem with containers built on M1 architecture and the need to build them on the linux/amd64 platform. Also, I sought help from a friend who works as a DevOps. He helped me to get confident with ssh connections and also helped to toggle the server’s system settings so everything could run smoothly.</li></p>
</ul>

## Route documentation

You can see the viewpoints and models on a root page (loacalhost:port/,port — the port for the app you set up manually or the default port for the app) by starting the app in a development config.

## Summary

This project is not perfect in any way. It was my first big project, so, once I have completed the main challenges, I decided to leave it as it is in order to continue learning and making new projects.

<i>Here starts the Readme in Russian.</i>

# Курсовая работа по Flask: онлайн-база кино

<p><b>Технологии:</b> Flask, PostgresQL, SQLAlchemy, Docker, SQLite.</p>

Это веб-приложение на Flask, оналйн-база кино с CRUD для фильмов, режиссеров, жанров и пользователей. В приложении есть функционал для авторизации и аутентификации пользователей. Зарегистрированные пользователи могут добавлять фильмы в избранное. Структура приложения (например, модуль с config factory, container, базовые DAO/service и модели) была предоставлена кураторами курса.

## Как запустить:
1. Скопируйте репозиторий на компьютер
2. В терминал введите следующие команды: <br>
`export FLASK_ENV=production` <br>
`export FLASK_APP=run.py` <br>
3. Запустите create_tables.py file
4. В терминале введите: <br>
`flask run`

## Трудности, с которыми я столкнулась
<ul>
<p><li>Разобраться в структуре, в которую нужно было вписать остатки проекта (всю логику, касающуюся пользователей и избранного), было непросто. Когда я занималась этим проектом, предоставленный код был сложен для понимания, потому что в программе не было теории для его полного понимания. Я разобралась достаточно для того, чтобы вписать свой код и даже править какие-то части изначального кода. С тех пор архитектура приложений на Flask стала одной из самых интересных и насущных для меня тем(так как я столкнулась с необходимостью продумывать ее в своем пет-проекте Reminder и до сих пор не нашла решения, которое меня бы устроило).</li></p>

<p><li>Другой трудностью была сама структура проекта. Правильно разделить логику проекта на три слоя и держать в голове, что происходит на каждом из них, было непросто. Со временем я к этому привыкла, хотя после проектов на Django она все равно выглядит очень сложной для меня.</li></p>

<p><li>Еще у меня возникла проблема с тестированием и автодокументацией функций, завернутых в декоратор <i>@security.auth_required</i>. Написать тесты мне помог коллега-сениор, а для документации я нашла решение в виде декоратора Flask-restx <i>@api.doc</i>.</li></p>

<p><li>Сложнее всего было автоматизировать развертку приложения на облачный сервер через Docker и GitHub actions, включая задачу создать вольюм для базы данных. В программе курса материала по Docker было мало, поэтому, чтобы лучше разобраться, я прошла отдельный мини-курс по Docker. После этого я смогла правильно настроить вольюм.
При развертке мне пришлось столкнуться с проблемами создания контейнеров на архитектуре M1 — на неокторых машинах они прокто не запускались. Решение, котороя я нашла — вручную задавать платформу linux/amd64 для создания контейнеров. Еще я попросила своего друга-ДевОпса помочь. Она помог мне разобраться с ssh-подключением и включить нужные системные настройки на сервере, чтобы все работало.</li></p>
</ul>

## Основные адреса

Подробный список адресов и моделей доступен в корне проекта (loacalhost:port/, port — заданный вами порт для приложения, либо порт приложения по умолчанию) после запуска приложения в режиме разработки.

## Дополнительно

Этот проект неидеален. Это был мой первый проект с большим числом модулей, поэтому, как только я закончила с основными задачами, я решила оставить его как есть, чтобы не тормозить обучение перейти к новым проектам.