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
                  'database': 'proj'}

        self.conn = mysql.connector.connect(**config)
        print("Good")
        self.cursor = self.conn.cursor()
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def mapper(self, entry: dict) -> KoreanWords:
        lexical_entry = KoreanWords(word=entry.get('word'),
                                     pos=entry.get('pos'),
                                     tfidf=entry.get('tfidf'),
                                     japanese=entry.get('japanese'),
                                     english=entry.get('english'))
        return lexical_entry

    def load_lexicon(self) -> KoreanWords:
        sql = 'SELECT * FROM korean'
        print("check")
        self.cursor.execute(sql)
        entries = [{'word': word,
                    'pos': pos,
                    'tfidf': tfidf,
                    'japanese': japanese,
                    'english': english
                    } for (word, pos, tfidf, japanese, english) in self.cursor]
        lexicon = [self.mapper(entry) for entry in entries]
        return lexicon

repo = MysqlRepository()
lexicon = repo.load_lexicon()
print(lexicon)