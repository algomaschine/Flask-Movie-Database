# Flask coursework

This is a web-app written with Flask framework. It imitates an online movie database with a CRUD for movies, directors, genres and users, authentication, and a possibility for a user to add movie to their favorites. The bone structure of the app (like config factory, container, base DAO/service layers for base models and overall module structure) was provided by the course tutors.

<p> <b>To launch:</b>
<br>1. Copy the repository onto your computer
<br>2. Run the following commands in terminal:
<br>export FLASK_ENV=production
<br>export FLASK_APP=run.py
<br>flask run -p 5002
<br><b>Or:</b>
<br>1. Copy the docker-compose.yml onto your computer
<br>2. From the folder with the file run docker-compose up
</p>

## Challenges
<ul>
<p><li>Getting my head around the pre-maid part of the project was not easy — it’s code was way ahead of the code I were taught on the cours at that time. I deciphered the pre-established parts of code decently enough to use them and integrate my own parts of code into it.</li></p>

<p><li>The other difficulty was the structure of the project itself. Having to divide the app logic into three layers and keep track of all of them was not easy. Eventually, I got used to it, but returning to this project after Django, I still find its structure to be very complicated.</li></p>

<p><li>I have also encountered a problem with testing and auto-documenting functions wrapped in the <i>@security.auth_required</i> decorator with Swagger. For testing functions, I sought the help of a senior developer. He helped me to write the tests for users' views. With Swagger, I came up up with somewhat of a fix using Flask-restx <i>@api.doc</i> decorator.</li></p>

<p><li>The most challenging part was to automate deploy of the app to the cloud server via Docker and GitHub actions, including the task to create a Docker volume for the database.
The course info on Docker was scarce, so, to understand it better, I took a Docker mini-course. It helped me create a volume for a database and get it to work properly.
Regarding deploy, I had to discover the problem with containers built on M1 architecture and the need to build them on the linux/amd64 platform. Also, I sought help from a friend who works as a DevOps. He helped me to get confident with ssh connections and also helped to toggle server’s system settings so everything could run smoothly.</li></p>
</ul>

## Route documentation

You can see the viewpoints and models on a root page by starting the app in a development config. Unfortunately, server that hosted the app is down now (because i needed to pay to keep it up).

## Summary

This project is not perfect in any way: it lacks type hints, mainly built with simple logic and, generally, not very well thought through. It was my first big project, so, once I have completed the main challenges, I decided to leave it as it is in order to continue learning and making new projects.
