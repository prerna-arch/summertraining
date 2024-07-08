
import datetime
import hashlib
class User:
    def __init__(self,name="",phone="",email="",password="",age=0,gender=""):
        self.name=name
        self.phone=phone
        self.email=email
        self.password=password
        self.age=age
        self.gender=gender
        self.created_on=datetime.datetime.now()

    def add_user(self):
          self.name=input("enter the user name:")
          self.phone=input("enter the user phone:")
          self.email=input("enter the user email:")
          self.password=input("enter the user password:").encode('utf-8')
          self.password=hashlib.sha256(self.password).hexdigest()
          self.age=input("enter the user age :")
          self.gender=input("enter the user gender :") 
"""
user=User()
user.add_user()
print(vars(user))
"""