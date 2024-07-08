
#from Session8B import DISHES 

class Menu():
    def __init__(self,name = "NA",number_of_dishes = "",menu_dishes=[]):
        #print("self hashcode:",self)
        self.name= name
        self.number_of_dishes= number_of_dishes
        self.menu_dishes= menu_dishes
        
    def show(self):
        print("------------------------------------")
        print("menu:{}|{}".format(self.name,self.number_of_dishes ))
        print("-----------------------------------------------")



        print("Dishes:")
        for idx in range(len(self.menu_dishes)):
            self.menu_dishes[idx].show()

#dishes= [DISHES(),DISHES("dal makahani",200,1,4.5,"inidan"),DISHES("chilli panner",300,2,5,"indian")]

#menu1 = Menu(name ="indian masala",number_of_dishes=len(dishes),menu_dishes=dishes)

#menu1.show()




