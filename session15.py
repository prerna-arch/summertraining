"""
customer manage ment system

create table Customer(
            cid int primary key auto_increment,
            name varchar(256),
            phone varchar(256),
            email varchar(256),
            age int(15),
            gender varchar(20),
            created_on datetime

);

"""
import datetime
class Customer:
    def __init__(self,cid=0,name="",phone="",email="",age=0,gender=""):
        self.cid= cid
        self.name= name
        self.phone=phone
        self.email=email
        self.age=age
        self.gender=gender
        self.created_on=datetime.datetime.now()


    def update_customer_details(self):
          name = input("enter customer name:")
          if len(name) != 0:
               self.name=name
          phone = input("enter customer phone:")
          if len(phone) != 0:
               self.phone=phone

          email = input("enter customer email:")
          if len(email) != 0:
               self.email=email

          age = input("enter customer age:")
          if len(age) != 0:
               self.age=int(age)

          gender = input("enter customer gender:")
          if len(gender) != 0:
               self.gender=gender





               
          

    def add_customer_details(self):
          self.name=input("enter the customer name:")
          self.phone=input("enter the customer phone:")
          self.email=input("enter the customer email:")
          self.age=input("enter the customer age :")
          self.gender=input("enter the customer gender :") 
          #we will not take input for created_on
          #created_on is a system date time stamp

    def show(self):
          print("---------------------customer details---------------------------")
          print("customer id:{}".format(self.cid))
          print("name:{}|phone:{}".format(self.name,self.phone))
          print("email:{}|age:{}".format(self.email,self.age))
          print("gender:{}".format(self.gender))
          print("created_on:{}".format(self.created_on))
          print("---------------------customer details---------------------------")


        