
"""
create table Patient(
            pid int primary key auto_increment,
            name varchar(256),
            phone varchar(256),
            email varchar(256),
            dob date,
            gender varchar(20),
            created_on datetime

);
"""

import datetime
class Patient:
    def __init__(self,pid=0,name="",phone="",email="",dob="",gender="",created_on=""):
        self.pid= pid
        self.name= name
        self.phone=phone
        self.email=email
        self.dob=dob
        self.gender=gender
        self.created_on=datetime.datetime.now()


    def update_Patient_details(self):
          name = input("enter Patient name:")
          if len(name) != 0:
               self.name=name
          phone = input("enter  Patient phone")
          if len(phone) != 0:
               self.phone=phone

          email = input("enter  Patient email:")
          if len(email) != 0:
               self.email=email

          dob= input("enter  Patient dob:")
          if len(dob) != 0:
               self.dob=(dob)   

          
          gender = input("enter  Patient gender:")
          if len(gender) != 0:
               self.gender=gender


    def add_pateint_details(self):
          self.name=input("enter the Pateint name:")
          self.phone=input("enter the Pateint phone:")
          self.email=input("enter the Pateint email:")
          self.dob=(input("enter the Pateint dob(yyyy-mm-dd):"))
          self.gender=input("enter the Pateint gender :") 
          #we will not take input for created_on
          #created_on is a system date time stamp

    def show(self):
          """
          print("---------------------Patient details---------------------------")
          print("Patient id:{}".format(self.pid))
          print("name:{}|phone:{}".format(self.name,self.phone))
          print("email:{}|dob:{}".format(self.email,self.dob))
          print("gender:{}".format(self.gender))
          print("created_on:{}".format(self.created_on))
          print("---------------------------------------------------------------")
          """
          patient="""
          {pid} | {name} |{phone}
          {email} | {dob}
          {gender} | {created_on} 
          """ .format_map(vars(self))
          print(patient)     
          