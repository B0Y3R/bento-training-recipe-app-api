FROM python:3.9.11-alpine3.15
MAINTAINER @B0Y3R

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# creates an empty folder
RUN mkdir /app

# switches to that as the default dir
WORKDIR /app

# copies local machine to app folder on image
COPY ./app /app

# create a user that will be used for running an application
RUN adduser -D user

# switches user to the user that we just created
USER user