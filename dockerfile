FROM python:3.7-alpine3.9
MAINTAINER Kevin Hernandez <kevteg05@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN apk --update add --virtual build-dependencies build-base libffi-dev postgresql-dev linux-headers bash
RUN mkdir /code
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
