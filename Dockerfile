FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /works

RUN pip install django

COPY . /works
