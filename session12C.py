class DISHES():
    #parameterized constructor with default values of arguments passed to it 
    def __init__(self,name = "NA",price = 0,quantity = 0,ratings = 0,catagoryofdish = "NA"):
        #print("self hashcode:",self)
        # copy the contents of name(input to constructor)to the self.name(attribute of object)
        self.name= name
        self.price= price
        self.ratings = ratings
        
    def show(self):
        print("------------------------------------")
        print("Dish:{}|{}|{}".format(self.name,self.price,self.ratings ))
