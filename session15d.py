#Database oops
import mysql.connector as db


class Database:

    def __init__(self):
        self.connection = db.connect(user="root",
                        password="omsairam3008",
                        host="127.0.0.1",
                        database="first1")
        print("[Database]connection created..")


        self.cursor = self.connection.cursor()
        print("cursor created..")

    def write(self,sql):
        print("[Database] sQL statement",sql)
        self.cursor.execute(sql)
        self.connection.commit()
        print("[Database] sQL statement")

        

    def read(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
        
        