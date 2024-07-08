"""
1.Execute some SQL commnds

object Relational Mapping(ORM)
#1.LIST DATABASE
show databases;


#2.crete your database
crete database first1;for creation of database

#3.select the database in which you want to create table
use first1;


#4.create table
create table customer;

#5 check that table is created
show table;

#6.view your table structure
describe customer;
 
create table customer(
     cid int primary key auto_increment,
     name varchar(256),
     phone varchar(15),
     email varchar(256),
     age int,
     gender varchar(10)

);

2. work with virtual env
3.installation of driver
4.sql coonection with python

customer:name,phone,email,age,gender,etc

"""
class customer:
    def __init__(self,name="NA",phone="na",email="na",age=0,gender="na"):
        self.name= name
        self.phone=phone
        self.email=email
        self.age=age
        self.gender=gender



    def add_customer_details(self):
          self.name=input("enter the customer name:")
          self.phone=input("enter the customer phone:")
          self.email=input("enter the customer email:")
          self.age=input("enter the customer age :")
          self.gender=input("enter the customer gender :")


    def show(self):
          print("---------------------customer details---------------------------")
          print("name:{}|phone:{}".format(self.name,self.phone))
          print("email:{}|age:{}".format(self.email,self.age))
          print("email:{}".format(self.age))
          print("---------------------customer details---------------------------")


"""
#create object :python
customer1=customer(name="john",phone="456789",email="john@gmail.com",age=20,gender="male")
print(vars(customer1))
"""


        

        