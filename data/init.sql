CREATE DATABASE IF NOT EXISTS proj;
ALTER DATABASE proj CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE proj;

CREATE TABLE korean (
    id INT NOT NULL AUTO_INCREMENT,
    word VARCHAR(30),
    tfidf FLOAT,
    japanese VARCHAR(30),
    english VARCHAR(30),
    pos VARCHAR(30),
    PRIMARY KEY (id)
);

INSERT INTO korean
    (word, tfidf, japanese, english, pos)
VALUES
    ('고려',0.3583133135037323,'考慮','Consideration',"['Noun']"),
    ('세율',0.2991603725486412,'関税','tariff',"['Noun']"),
    ('주택',0.297861543455624,'ハウジング','Housing',"['Noun']"),
    ('검토정부','0.1791566567518661','レビュアー','Reviewer',"['Noun', 'Noun']");
