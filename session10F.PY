
#from session10d import Driver
#from Session10C  import Vehicle
class customer:
    def __init__(self,name ="NA",phone_number="NA",email="NA",address="NA",gender="NA",age="NA"):
        self.name=name
        self.phone_number=phone_number
        self.email=email
        self.address=address
        self.gender=gender
        self.age=age

    def add_customer_details(self):
        self.name=input("enter the customer name:")
        self.phone_number=input("enter the customer phone number:")
        self.email=input("enter the customer email:")
        self.address=input("enter the customer address:")
        self.gender=input("enter the gender :")
        self.age=input("enter the customer age:")

    def show(self):
        print("-------------------customer details-----------------------------")
        print("name:{}|phone_number:{}".format(self.name,self.phone_number))
        print("email:{}|address:{}".format(self.email,self.address))
        print(" gender:{}".format(self.gender))
        print(" age:{}".format(self.age))

        print("------------------------------------------------")


    def to_csv(self):
        data="{},{},{},{},{},{} \n".format(self.name,self.phone_number,self.email,self.address,self.gender,self.age)
        return data

"""
customer1 = customer()
customer1.add_customer_details()
customer1.show()

driver = Driver()
driver.add_driver_details()
driver.show()

vehicle=Vehicle()#object creation
vehicle.add_vehicle_details() 
vehicle.show()
"""