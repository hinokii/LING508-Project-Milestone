import mysql.connector
from db.repository import *
from model.word import *

class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()

        config = {'user': 'root',
            	  'passwd': 'test',
                  'host': 'localhost',
                  'port': '32000',
                  'database': 'project'}

        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()

    def mapper(self, entry: dict) -> KoreanWord:
        korean_word = KoreanWord()
        korean_word.word = entry['word']
        korean_word.tfidf = entry['tfidf']
        korean_word.japanese = entry['japanese']
        korean_word.english = entry['english']
        korean_word.pos = entry['pos']
        '''
        lexical_entry = KoreanWords(word=entry('word'),
                                     tfidf=entry.get('tfidf'),
                                     japanese=entry.get('japanese'),
                                     english=entry.get('english'),
                                    pos=entry.get('pos'))
        '''
        return korean_word

    def insert_table(self, list1, list2, list3, list4, list5):
        """CREATE DATABASE IF NOT EXISTS project""";
        korean_doc = """CREATE TABLE IF NOT EXISTS korean (word VARCHAR(50), tfidf FLOAT, japanese VARCHAR(50), 
                                                                         english VARCHAR(50), pos VARCHAR(50))"""
        self.cursor.execute(korean_doc)
        self.cursor.execute("ALTER TABLE korean CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci")

        sql = "INSERT INTO korean VALUES (%s, %s, %s, %s, %s)"

        for i in range(len(list1)):
            self.cursor.execute(sql, (list1[i], list2[i], list3[i], list4[i], list5[i]))

        self.conn.commit()

    def load_lexicon(self) -> KoreanWords:
        sql = 'SELECT * FROM korean'
        print("check")
        self.cursor.execute(sql)
        entries = [{'word': word,
                    'tfidf': tfidf,
                    'japanese': japanese,
                    'english': english,
                    'pos': pos,
                    } for (word, tfidf, japanese, english, pos) in self.cursor]

        lexicon = [self.mapper(entry) for entry in entries]
        return entries

    #def __del__(self):
        #self.cursor.close()
        #self.conn.close()
'''
import pandas as pd
df = pd.read_csv('df.csv', index_col=0)

tfidfs = df['tfidf'].tolist()
words = df.index.values.tolist()
pos = df['POS'].tolist()
eng = df['English'].tolist()
jp = df['Japanese'].tolist()

repo = MysqlRepository()
repo.insert_table(words, tfidfs, jp, eng, pos)
result = repo.load_lexicon()
print(result[:5])
'''