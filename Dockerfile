FROM python:3.9

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

#CMD tail -f /dev/null

FROM node:6-slim
RUN mkdir -p /usr/share/man/man1
    echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/backports.list && \
    apt-get update -y && \
    apt-get install -t jessie-backports openjdk-8-jdk -y
