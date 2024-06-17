"""
Principle of oops:
1.think of an object
meesho my order:order id,seller name,address,phone number,delivery date ,shiiping date,placed date,total price


"""
# 2.create class of object
#3. below class represents the object.its is description of object

class my_order:
    pass




#3 create the real object from  class in memory
#below  is:object construction statement
order1 = my_order()
order2 = my_order()
#reference copy operation
order3 = order2
# order is a refernce variable,my_order()- represent the object construction
print(order1)


#WRITE OPERATION

order1.orderid = 2345
order1.sellername = "Harsimran"
order1.address = "dhashmesh nagar"
order1.phonenumber = 1234

order2.orderid = 2345
order2.sellername = "Harsimran"
order2.address = "dhashmesh nagar"
order2.phonenumber = 1234
order2.delivery = " 10 july,2024"
order2.shipping = " 8 july ,2024"

#update operation

order1.orderid = 5789

#read operation
print("my order data:")
print(vars(order1))
print(vars(order2))


del order1.address


print(vars(order1))
print(vars(order3))




