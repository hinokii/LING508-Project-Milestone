import mysql.connector
from process import *

class Database:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

        self.conn = mysql.connector.connect(user='root',
                               host='mysql',
                               passwd='sakila',
                               port='3306')
        '''
        For local use
        self.conn = mysql.connector.connect(user='root',
                                            host='localhost',
                                            passwd='sakila',
                                            port='32000',
                                            database='project'
                                        )
        '''
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE DATABASE project")
        self.conn = mysql.connector.connect(user='root',
                               host='mysql',
                               passwd='sakila',
                               port='3306',
                               database='project')
        self.cursor = self.conn.cursor()

    def create_database(self, tablename, col1, col2):
        # Connecting from the server

        korean_doc = """CREATE TABLE IF NOT EXISTS {0} ({1} VARCHAR(50), {2} FLOAT)""".format(tablename, col1, col2)
        self.cursor.execute(korean_doc)
        self.cursor.execute("ALTER TABLE {} CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci".format(tablename))

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


