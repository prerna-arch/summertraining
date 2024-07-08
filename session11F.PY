from session10d import Driver
#from Session10C import Vehicle
from session11E import Ride
from session10F  import customer


#driver application
driver = Driver()
driver.add_driver_details()

#customer application
customer1 = customer()
customer1.add_customer_details()

#server
ride=Ride()
ride.add_ride_details()
ride.link_customer(customer1)
ride.link_driver(driver)


print("RIDE BOOKED....")
ride.show()

