FROM python:3.8

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

#CMD tail -f /dev/null

RUN apt-get update && \
    apt-get install -y curl \
    wget \
    openjdk-11-jdk

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/bin/java

CMD python app.py
