FROM python:3.8-alpine

ARG run_env=development

ENV env $run_env

LABEL "author"="zhnec"

WORKDIR /urs/src/my_test

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD pytest -m "$env" -s -v tests/*
