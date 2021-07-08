FROM alpine:latest
MAINTAINER DCVDS

RUN addgroup -S galaxy && adduser -S hive -G galaxy
USER root

RUN apk --no-cache upgrade
RUN apk update && apk add bash

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip install websockets

EXPOSE 80

WORKDIR /home
COPY command.sh /home
COPY hive.py /home

ENTRYPOINT ["/bin/sh", "/home/command.sh"]
