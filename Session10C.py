"""
driver has a vehicle
customer can book ride(s)


driver:name,phone_number,email,liscense,rating,gender,age,vehicle[1 to1]

1 driver has 1 vehicle

vehicle:vehicle no,model,color,brand
customer:name,phone_number,email,address,gender,age
ride:customer[1 to 1],data,time,from_loc,to-loc,distance,fare,driver[1 to 1]
1 ride has 1 customer
1 ride has 1 driver
"""

class Vehicle:
    def __init__(self,reg_no ="NA",model="NA",color="white",brand=" NA"):
        self.reg_no=reg_no
        self.model=model
        self.color=color
        self.brand=brand

    def add_vehicle_details(self):
        self.reg_no=input("enter the vehicle  reg no")
        self.model=input("enter the vehicle  model")
        self.color=input("enter the vehicle  color")
        self.brand=input("enter the vehicle  brand")

    def show(self):
        print("------------------vehicle details------------------------------")
        print("reg number:{}|model:{}".format(self.reg_no,self.model))
        print("color:{}|brand:{}".format(self.reg_no,self.brand))
        print("------------------------------------------------")




        