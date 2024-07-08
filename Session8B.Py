










#class for object DISHES
class DISHES():
    #parameterized constructor with default values of arguments passed to it 
    def __init__(self,name = "NA",price = 0,quantity = 0,ratings = 0,catagoryofdish = "NA"):
        #print("self hashcode:",self)
        # copy the contents of name(input to constructor)to the self.name(attribute of object)
        self.name= name
        self.price= price
        self.quantity = quantity
        self.ratings = ratings
        self.catagoryofdish = catagoryofdish
    def show(self):
        print("------------------------------------")
        print("Dish:{}|{}|{}|{}|{}".format(self.name,self.price,self.quantity,self.ratings,self.catagoryofdish ))

dish = DISHES()#object creation
#print("dish hashcode:",dish)
print("----------------------------------------------------------------------------------")
dish1 = DISHES("dal makahani",200,1,4.5,"inidan")
#print("dish1 hashcode:",dish1)
print("----------------------------------------------------------------------------------")
dish2 = DISHES("chilli panner",300,2,5,"indian")
#print("dish2 hashcode:",dish2)
print("----------------------------------------------------------------------------------")


#dish.show()
#dish1.show()
#dish2.show()

#list of dishes
#dishes =[dish,dish1,dish2]
#dishes = [DISHES(),DISHES("dal makahani",200,1,4.5,"inidan"),DISHES("chilli panner",300,2,5,"indian")]


#for idx in range(len(dishes)):
    #dishes[idx].show()

