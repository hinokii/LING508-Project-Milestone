FROM python:3.9
FROM ubuntu: 16.04# install packages

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

#CMD tail -f /dev/null


RUN apt-get update && \
    apt-get install -y curl \
    wget \
    openjdk-8-jdk
    
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java

