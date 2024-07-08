"""
Principle of oops:
1.think of an object
meesho my order:order id,seller name,address,phone number,delivery date ,shiiping date,placed date,total price


"""
# 2.create class of object
#3. below class represents the object.its is description of object

class my_order:
    # Default constructor in python
    # self is reference variable,which will hold the hashcode of current object .
    
      def __init__(self):
        print("self:",self)
        self.orderid = 2345
        self.sellername = "Harsimran"
        self.address = "dhashmesh nagar"
        self.phonenumber = 1234
        

        #parameterized constructor
      def __init__(self,orderid,sellername,address,phonenumber):
            print("self:",self)
            self.orderid = orderid
            self.sellername = sellername
            self.address = address
            self.phonenumber = phonenumber

"""
      def show(self):
                 print("----------------------------")
                 print("order1 data:")
                 print("order id:",self.orderid)
                 print("-----------------------------------")
 """             
print("----------------------------------------------")   
order1 = my_order("1234","harsimran","dhashmesh","4567")
print("order1:",order1)
print("order1  data:")
print(vars(order1))
#order1.show()
print("------------------------------------------------")  

order2 = my_order("2334","prerna","sashtri nagar","8906")
print("order2:",order2)
print("order2 data:")
print(vars(order2))
#order2.show()
print("-------------------------------------------------")  

#throw error
#order3 = my_order()

"""
hw:
code below 3 objects
    restaurent
    menu
    dish

"""




