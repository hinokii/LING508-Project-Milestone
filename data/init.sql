DROP DATABASE IF EXISTS proj;
CREATE DATABASE proj;
ALTER DATABASE proj CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE proj;

CREATE TABLE korean (
    id INT NOT NULL AUTO_INCREMENT,
    word NVARCHAR(30),
    tfidf FLOAT,
    japanese NVARCHAR(30),
    english VARCHAR(30),
    pos VARCHAR(30),
    PRIMARY KEY (id)
);

INSERT INTO korean
    (word, , tfidf, japanese, english, pos
VALUES
    (N'고려', 0.3583133135037323, N'考慮', 'Consideration',"['Noun']"),
    (N'세율', 0.2991603725486412, N'関税', 'tariff',"['Noun']"),
    (N'주택', 0.297861543455624, N'ハウジング', 'Housing',"['Noun']"),
    (N'검토정부', 0.1791566567518661', N'レビュアー', 'Reviewer',"['Noun', 'Noun']");
