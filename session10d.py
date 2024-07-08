

from Session10C import Vehicle

class Driver:
    def __init__(self,name="NA",
                 phone_number="NA",
                 email="NA",liscense="NA",rating=2.5,gender="NA",age=18,vehicle=None):
        self.name=name
        self.phone_number=phone_number
        self.email=email
        self.liscense=liscense
        self.rating=rating
        self.gender=gender
        self.age=age
        self.vehicle=vehicle
    

    def add_driver_details(self):
        self.name=input("enter the driver name:")
        self.phone_number=input("enter the driver phone:")
        self.email=input("enter the email:")
        self.liscense=input("enter the lisecence:")
        self.rating=input("enter the rating:")
        self.gender=input("enter the gender:")
        self.age=input("enter the age:")
        #1 to 1 mapping
        #1 driver has 1 vehicle
        self.vehicle=Vehicle()#object creation
        self.vehicle.add_vehicle_details()
    def show(self):
        print("-------------------driver details-----------------------------")
        print(" name:{}|phone:{}".format(self.name,self.phone_number))
        print(" email:{}|liscense:{}".format(self.email,self.liscense))
        print(" rating:{}|gender:{}".format(self.rating,self.gender))
        print(" age:{}".format(self.age))

        print("------------------------------------------------")
        
        self.vehicle.show()

#driver = Driver()
#driver.add_driver_details()
#driver.show()

    

        