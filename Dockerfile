FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY .env /code/

RUN pip install -r requirements.txt
COPY . /code/
