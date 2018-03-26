FROM python:3.6-alpine

RUN apk add --update postgresql-dev \
    gcc \
    python3-dev \
    musl-dev && \
    pip3 install psycopg2
    