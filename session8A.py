"""
Principle of oops:
1.think of an object
meesho my order:order id,seller name,address,phone number,delivery date ,shiiping date,placed date,total price


"""
# 2.create class of object
#3. below class represents the object.its is description of object

class my_order:
    def __init__(self):
        print("self:",self)
        self.orderid = 2345
        self.sellername = "Harsimran"
        self.address = "dhashmesh nagar"
        self.phonenumber = 1234

order1 = my_order()
print(order1)
       

