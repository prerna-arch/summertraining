from Session8B import DISHES
from session9A  import  Menu

class Restaurent():
    def __init__(self,name = "NA",phone = "NA",email = "NA",address = "NA",operating_hour ="10;00 to 11;00",ratings=" 2.5",menu = None):
        #print("self hashcode:",self)
        self.name= name
        self.phone = phone 
        self.email= email
        self.address=address
        self.operating_hour=operating_hour 
        self.ratings=ratings
        self.menu = menu

        
    def show(self):
        print("------------------------------------")
        print("RESTAURENT:")
        print("Restaurent:{}|{}|{}|{}|{}|{}|".format(self.name,self.phone,self.email,self.address,self.operating_hour,self.ratings))
        print("-----------------------------------------------")



        self.menu.show()


#dishes= [DISHES(),DISHES("dal makahani",200,1,4.5,"inidan"),DISHES("chilli panner",300,2,5,"indian")]

#menu1 = Menu(name ="indian masala",number_of_dishes=3,menu_dishes=dishes)

#Res =  Restaurent(name="ludhiana veggie",phone="998888",email="sabprer",address="civillines",ratings="5.5",menu=menu1)   
#Res.show()  
"""
Res =  Restaurent(name="ludhiana veggie",
                  phone="998888",
                  email="sabprer",
                  address="civillines",
                  ratings="5.5",
                  menu = Menu(name ="indian masala",
                            number_of_dishes=3,
                            menu_dishes=[DISHES(),
                                         DISHES("dal makahani",200,1,4.5,"inidan"),
                                         DISHES("chilli panner",300,2,5,"indian")]
))   
Res.show()"""
Restaurent(name="ludhiana veggie",
                  phone="998888",
                  email="sabprer",
                  address="civillines",
                  ratings="5.5",
                  menu = Menu(name ="indian masala",
                            number_of_dishes=3,
                            menu_dishes=[DISHES(),
                                         DISHES("dal makahani",200,1,4.5,"inidan"),
                                         DISHES("chilli panner",300,2,5,"indian")]
)).show()