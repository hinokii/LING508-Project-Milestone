FROM python:3.9

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

#CMD tail -f /dev/null

FROM centos:8

ENV PATH=$PATH:/opt/java/jdk-15.0.2/bin

WORKDIR /opt/java

RUN curl https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_linux-x64_bin.tar.gz -o openjdk-15.0.2_linux-x64_bin.tar.gz

RUN tar -xzf openjdk-15.0.2_linux-x64_bin.tar.gz && \
    rm -rf openjdk-15.0.2_linux-x64_bin.tar.gz
