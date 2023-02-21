FROM python:3.10

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./project ./project
COPY ./volumes ./volumes
COPY run.py .
COPY project.db .
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

CMD flask run -h 0.0.0.0 -p 80
