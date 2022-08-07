FROM python:3.8

COPY . .

FROM postgres:9.4
COPY /PycharmProjects/pythonProject1/data/docker-entrypoint-initdb.d

RUN pip install -U pip
RUN pip install -r requirements.txt

#CMD tail -f /dev/null

RUN apt-get update && \
    apt-get install -y curl \
    wget \
    openjdk-11-jdk

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/bin/java


