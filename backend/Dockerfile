# syntax=docker/dockerfile:1
FROM python:3.7-alpine
RUN mkdir backend
WORKDIR /backend
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=127.0.0.1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . ./backend
CMD ["flask", "run"]
