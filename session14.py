import mysql.connector as db
from session13 import customer
#Database username and password
#username = "root"
#password =""

#local host
#host="27.0.0.1"
#database ="first1"





#1.create connection

connection = db.connect(user="root",
                        password="omsairam3008",
                        host="127.0.0.1",
                        database="first1")
print("connection created..")
print(connection)
"""
customer1=customer()
customer1.add_customer_details()
"""
#2 create sql statement
#sql = "insert into customer values(null,'{}','{}','{}',{},'{}')".format(customer1.name,customer1.phone,customer1.email,customer1.age,customer1.gender)
#sql = "insert into restaurent values('sweet temptation','5.6','4567','ghumar mandi','sweet@gmail',null)"
#sql= "update customer set name ='sia',gender='female',email='sia@gmail'where cid = 2"
sql="delete from customer where cid=2"
#3: obtain cursor -> perform crud operations with mysql
cursor = connection.cursor()

#4 execute sql command
cursor.execute(sql)
#5 commit the write operation
connection.commit()

print("sql statement executed")
