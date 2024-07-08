"""
oops case study:food delivery app
Customer:name,phone,email,order,address
Dish:name,rating,price
Order:orderid,Dish,bill

1 Customer have many orders
1 Order can have many Dishes

"""

class Customer:
     def __init__(self,name="NA",phone="NA",email="NA",order="None",address="NA"):
          self.name=name
          self.phone=phone
          self.email=email
          self.order=order
          self.address=address


     def add_customer_details(self):
          self.name=input("enter the customer name:")
          self.phone=input("enter the customer phone:")
          self.email=input("enter the customer email:")
          self.address=input("enter the customer address :")


     def show(self):
          print("---------------------customer details---------------------------")
          print("name:{}|phone:{}".format(self.name,self.phone))
          print("email:{}|address:{}".format(self.email,self.address))
     
     
          

          
          
