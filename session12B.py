
#1 order can have 1 customer and 1 order can have many dishes
class Order:
     def __init__(self,orderid="NA",Dishes=None,customer=None,bill=0):
          self.orderid=orderid
          self.Dishes=Dishes
          self.customer=customer
          self.bill=bill
          

     def show(self):
          print("-----------------order details-----------------------")
          print("order id:{}|bill:{}".format(self.orderid,self.bill))
          print("-----------------order details-----------------------")

          print("order placed by:")
          self.customer.show()

          print("order dishes")
          for dish in self.Dishes:
               dish.show()

"""
     def link_dishes(self, Dishes):
        self.Dishes = Dishes

        for dish in self.Dishes:
            
             self.total += dish.price
            
     def link_customer(self, customer):

          self.customer = customer

"""
    
          
     