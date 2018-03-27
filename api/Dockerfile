FROM python:3.6-alpine

RUN apk add --update postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    && rm -rf /var/cache/apk/*
    
RUN pip3 install psycopg2 bs4 requests