


class Ride:
    def __init__(self,customer=None,date="20th june,2024",time="12:00",from_loc="home",to_loc="work",distance=4,fare=200,driver=None):
        self.customer=customer
        self.date=date
        self.time=time
        self.from_loc=from_loc
        self.to_loc=to_loc
        self.distance=distance
        self.fare=fare
        self.driver=driver        


    def add_ride_details(self):
        print(">> enter ride details")
        self.from_loc=input("enter from location:")
        self.to_loc=input("enter to location")
        
    def link_driver(self,driver):
        self.driver=driver

    def link_customer(self,customer):
        self.customer=customer

        
    def show(self):
        self.customer.show()
         
        print("------------------RIDE-----------------")    
        print("FROM: {} | TO: {}".format(self.from_loc, self.to_loc))
        print("DISTANCE: {} | FARE: {}".format(self.distance , self.fare))
        print("DATE: {} | TIME: {}".format(self.date, self.time))
        
        print("------------------------------------------")

        self.driver.show()
