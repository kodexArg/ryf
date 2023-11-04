# pull official base image
FROM python:3.12-slim-bookworm

# set work directory for config
WORKDIR /usr/src/config

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install os dependencies
RUN apt update
RUN apt install -y vim gcc default-libmysqlclient-dev pkg-config python3-dev

# copy configurations and requirements to config directory
COPY ./config/gunicorn.config.py .
COPY ./config/requirements.txt .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /usr/src/app