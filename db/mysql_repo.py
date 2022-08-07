import mysql.connector
from db.repository import *
from model.word import *

class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()
        '''
        #For local use
        config = {'user': 'root',
            	  'passwd': 'test',
                  'host': 'localhost',
                  'port': '32000',
                  'database': 'project'}
        '''
        config = {'user': 'root',
            	  'passwd': 'test',
                  'host': 'mysql',
                  'port': '3306',
                  'database': 'project'}

        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()

    def korean_mapper(self, entry: dict) -> KoreanWord:
        korean_word = KoreanWord()
        korean_word.word = entry['word']
        korean_word.tfidf = entry['tfidf']
        korean_word.japanese = entry['japanese']
        korean_word.english = entry['english']
        korean_word.pos = entry['pos']

        return korean_word

    def insert_korean_table(self, list1, list2, list3, list4, list5):
        # The following three lines of code is not needed when running locally since data/init.db properly runs
        # when docker-compose up based on docker-compose.yml, but on github, it doesn't seem to initial
        # data/init.db so I have to manually create table here. I think I need to add it to github action,
        # but not sure how.
        korean_doc = """CREATE TABLE IF NOT EXISTS korean (word VARCHAR(50), tfidf FLOAT, japanese VARCHAR(50),
                                                                         english VARCHAR(50), pos VARCHAR(50))"""
        self.cursor.execute(korean_doc)
        self.cursor.execute("ALTER TABLE korean CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci")

        sql = "INSERT INTO korean VALUES (%s, %s, %s, %s, %s)"

        for i in range(len(list1)):
            self.cursor.execute(sql, (list1[i], list2[i], list3[i], list4[i], list5[i]))

        self.conn.commit()

    def create_korean_dict(self):
        sql = 'SELECT * FROM korean'
        self.cursor.execute(sql)
        entries = [{'word': word,
                    'tfidf': tfidf,
                    'japanese': japanese,
                    'english': english,
                    'pos': pos,
                    } for (word, tfidf, japanese, english, pos) in self.cursor]
        return entries

    def load_korean_lexicon(self) -> KoreanWords:
        entries = self.create_korean_dict()
        lexicon = [self.korean_mapper(entry) for entry in entries]
        return lexicon

    def del_korean_table(self):
        sql = "DROP TABLE korean"
        self.cursor.execute(sql)
        self.cursor.close()
        self.conn.close()

    def japanese_mapper(self, entry: dict) -> JapaneseWord:
        japanese_word = JapaneseWord()
        japanese_word.word = entry['word']
        #japanese_word .tfidf = entry['tfidf']
        japanese_word.korean = entry['korean']
        japanese_word.english = entry['english']
        japanese_word.pos = entry['pos']

        return japanese_word

    def insert_japanese_table(self, list1, list2, list3, list4):
        # The following three lines of code is not needed when running locally since data/init.db properly runs
        # when docker-compose up based on docker-compose.yml, but on github, it doesn't seem to initial
        # data/init.db so I have to manually create table here. I think I need to add it to github action,
        # but not sure how.
        #japanese_doc = """CREATE TABLE IF NOT EXISTS japanese (word VARCHAR(50), korean VARCHAR(50),
                                                                         #english VARCHAR(50), pos VARCHAR(50))"""
        #self.cursor.execute(japanese_doc)
        self.cursor.execute("ALTER TABLE japanese CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci")

        sql = "INSERT INTO japanese VALUES (%s, %s, %s, %s)"

        for i in range(len(list1)):
            self.cursor.execute(sql, (list1[i], list2[i], list3[i], list4[i]))

        self.conn.commit()

    def create_japanese_dict(self):
        sql = 'SELECT * FROM japanese'
        self.cursor.execute(sql)
        entries = [{'word': word,
                    #'tfidf': tfidf,
                    'korean': korean,
                    'english': english,
                    'pos': pos,
                    } for (word, korean, english, pos) in self.cursor]
        return entries

    def load_japanese_lexicon(self) -> JapaneseWords:
        entries = self.create_japanese_dict()
        lexicon = [self.japanese_mapper(entry) for entry in entries]
        return lexicon

    def del_japanese_table(self):
        sql = "DROP TABLE japanese"
        self.cursor.execute(sql)
        self.cursor.close()
        self.conn.close()



