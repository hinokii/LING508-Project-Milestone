import mysql.connector
#from process import *

class Database:
    def __init__(self, list1, list2, list3, list4, list5):
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3
        self.list4 = list4
        self.list5 = list5
       
        self.conn = mysql.connector.connect(user='root',
                               host='mysql',
                               passwd='sakila',
                               port='3306')
        '''
        #For local use
        self.conn = mysql.connector.connect(user='root',
                                            host='localhost',
                                            passwd='sakila',
                                            port='32000',
                                            database='project'
                                        )
        '''
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS project")
        self.conn = mysql.connector.connect(user='root',
                               host='mysql',
                               passwd='sakila',
                               port='3306',
                               database='project')
                               
        self.cursor = self.conn.cursor()
        
    def create_database(self, tablename, col1, col2, col3, col4, col5):
        # Connecting from the server

        korean_doc = """CREATE TABLE IF NOT EXISTS {0} ({1} VARCHAR(50), {2} FLOAT, {3} VARCHAR(50), {4} VARCHAR(50),
                        {5} VARCHAR(50))""".format(tablename, col1, col2, col3, col4, col5)
        self.cursor.execute(korean_doc)
        self.cursor.execute("ALTER TABLE {} CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci".format(tablename))

        sql = "INSERT INTO {0} ({1}, {2}, {3}, {4}, {5})\
        VALUES (%s, %s, %s, %s, %s)".format(tablename, col1, col2, col3, col4, col5)

        for i in range(len(self.list1)):
            self.cursor.execute(sql, (self.list1[i], self.list2[i], self.list3[i], self.list4[i], self.list5[i]))

        self.conn.commit()

    def retrive_data(self, tablename):
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


