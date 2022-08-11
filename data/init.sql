DROP DATABASE IF EXISTS project;
CREATE DATABASE project;
ALTER DATABASE project CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE project;

CREATE TABLE korean (
    word NVARCHAR(30),
    tfidf FLOAT,
    japanese NVARCHAR(30),
    english VARCHAR(30),
    pos VARCHAR(30)
    );

CREATE TABLE japanese (
    word NVARCHAR(30),
    tfidf FLOAT,
    korean NVARCHAR(30),
    english VARCHAR(30),
    pos VARCHAR(30)
    );

