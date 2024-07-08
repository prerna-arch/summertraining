class DISHES():
    #parameterized constructor with default values of arguments passed to it 
    def __init__(self,name = "NA",price = 0,ratings = 0):
        #print("self hashcode:",self)
        # copy the contents of name(input to constructor)to the self.name(attribute of object)
        self.name= name
        self.price= price
        self.ratings = ratings
        
    def show(self):
        print("------------------------------------")
        print("Dish:{}|{}|{}".format(self.name,self.price,self.ratings ))


def bubblesort(data):

     for i in range(0,len(data)):
          
        for j in range(i+1,len(data)):

         if data[j].price<data[i].price:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp

def bubblesort1(data):

     for i in range(0,len(data)):
          
        for j in range(i+1,len(data)):

         if data[j].ratings>data[i].ratings:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp

     
"""
dish = DISHES("Tadka panner",600,3.4)#object creation
#print("dish hashcode:",dish)
print("----------------------------------------------------------------------------------")
dish1 = DISHES("dal makahani",200,4.5)
#print("dish1 hashcode:",dish1)
print("----------------------------------------------------------------------------------")
dish2 = DISHES("chilli panner",300,5)
#print("dish2 hashcode:",dish2)
print("----------------------------------------------------------------------------------")
"""
dishes=[DISHES("Tadka panner",600,3.4),
       DISHES("dal makahani",200,4.5) ,
        DISHES("chilli panner",300,5)]
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for dish in dishes:
    dish.show()

print("\n~~~~~~~~~~~~~~Sort according to price~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``")

bubblesort(dishes)
for dish in dishes:
    dish.show()

print("\n~~~~~~~~~~~~~~Sort according to ratings~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``")   

bubblesort1(dishes)
for dish in dishes:
    dish.show()



