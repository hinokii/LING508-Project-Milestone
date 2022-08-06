FROM python:3.9
FROM openjdk:11

COPY . .
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp

#RUN pip install -U pip
RUN pip install -r requirements.txt
RUN javac Main.java
CMD ["java", "Main"]
#CMD tail -f /dev/null



