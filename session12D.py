from session12C import DISHES
from session12B import Order
from session12  import Customer


dishes=[DISHES("Tadka panner",600,3.4),
       DISHES("dal makahani",200,4.5) ,
        DISHES("chilli panner",300,5)]

Customer1=Customer(name="john",phone="56789",email="john@gmail.com",address="southcity")
Customer2=Customer(name="aims",phone="1234",email="sam@gmail.com",address="shanes")

#Hard Coding: We as developer are linking objects
order=Order(orderid="1",Dishes=[dishes[0],dishes[2]],customer=Customer1,bill=550)
order.show()

"""
order1 = Order(orderid=1)
order1.link_customer(customer= Customer1)
order1.link_dishes(Dishes=[dishes[0], dishes[2]])

order2 = Order(orderid=2)
order2.link_customer(customer= Customer1)
order2.link_dishes(Dishes=[dishes[0], dishes[1], dishes[2]])

order1.show()
order2.show()

"""