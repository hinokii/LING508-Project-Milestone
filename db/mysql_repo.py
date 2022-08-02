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
        self.cursor = self.conn.cursor()
    #def __del__(self):
        #self.cursor.close()
        #self.conn.close()

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

    def load_lexicon(self) -> KoreanWords:
        sql = 'SELECT * FROM korean'
        print("check")
        self.cursor.execute(sql)
        entries = [{'id': id,
                    'word': word,
                    'tfidf': tfidf,
                    'japanese': japanese,
                    'english': english,
                    'pos': pos,
                    } for (id, word, tfidf, japanese, english, pos) in self.cursor]

        lexicon = [self.mapper(entry) for entry in entries]
        return entries



