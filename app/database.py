import mysql.connector
#from process import *

class Database:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

        try:
            self.conn = mysql.connector.connect(user='root',
                               host='mysql',
                               passwd='test',
                               port='3306',
                               database='project')

            self.cursor = self.conn.cursor()

        except:
            return "Cannot connect to mysql!"

    def create_database(self, tablename, col1, col2):
        # Connecting from the server

        korean_doc = """CREATE TABLE IF NOT EXISTS {0} ({1} VARCHAR(50), {2} FLOAT)""".format(tablename, col1, col2)
        self.cursor.execute(korean_doc)


        sql = "INSERT INTO {0} ({1}, {2})\
        VALUES (%s, %s)".format(tablename, col1, col2)

        for i in range(len(self.list1)):
            self.cursor.execute(sql, (self.list1[i], self.list2[i]))

        self.conn.commit()


    def retrive_data(self, tablename, col_name):
        sql = "SELECT * FROM {}".format(tablename)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def deleted_table(self, tablename):
        try:
            sql = "DROP TABLE {}".format(tablename)
            self.cursor.execute(sql)
            self.conn.close()
        except:
            return "can't delete"
'''
text = open('web_data.txt', 'r').read()
tk = TokenizeKoreanSent(text)
tokenized = tk.tokenize_korean()
tfidf = TFIDF(tokenized)
df = tfidf.create_pandas_word_and_tfidf()
tfidfs = df['tfidf'].tolist()
words = df.index.values.tolist()

db = Database(words, tfidfs)
#data = db.create_database("korean_t", "word", 'tfidf')
result = db.retrive_data("korean_t", 't')





db = Database(words, tfidfs)
db.deleted_table('k_t')
'''
