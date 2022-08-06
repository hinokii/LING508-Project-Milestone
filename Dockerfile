FROM python:3.9

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

#CMD tail -f /dev/null

FROM ubuntu: 16.04# install packages
RUN apt-get update && \
    apt-get install -y curl \
    wget \
    openjdk-8-jdk

