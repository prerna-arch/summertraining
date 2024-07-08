"""
restaurent:name,location,ratings,catagory,phone number,opening hours,closing hours,image
menu:catagory of menu,types of menu,dishes in menu
DISH:name,price,quantity,image,ratings,catagory of dish

"""
print("----------------------------------------------------------------------------------")
class restaurent():
    def __init__(self):
        print("self hashcode:",self) 
        self.name = "blossam "
        self.location = "civil lines,ludhiana"
        self.ratings = "4.5 \u2605"
        self.catagory = "vegetarian"
        self.phonenumber = "7890xxxxxx"
        self.openinghours =  "12noon"
        self.closinghours = "8pm"

res = restaurent()#object creation
print("res hashcode:",res)
print("-------------------------------------------------------------------------------")
print("\u2728 RESTAURENT DETAILS: \u2728","\n")
print("Name of restaurent:",res.name,"\u2698","\n","Location:",res.location,"\n","Ratings:",res.ratings,"\n","Catagory:",res.catagory,"\n","Phone number:",res.phonenumber,"\n","Opening hours:",res.openinghours,"\n","Closing hours:",res.closinghours)
print("---------------------------------------------------------------------------------")

class menu():
    def __init__(self):

        print("self hashcode:",self)
        self.Catagory = "SOUTH INDIAN"
        self.Typesofmenu = "SOUTH INDIAN/PUNJABI/BENGALI"
        self.dishesavailable = 300

menu1 = menu()#object creation
print("menu1 hashcode:",menu1)
print("----------------------------------------------------------------------------------")
print(" \u2728 MENU \u2728 \n")
print("Catagory:",menu1.Catagory,"\n","Types of menu:",menu1.Typesofmenu,"\n","Dishes available:",menu1.dishesavailable)
print("--------------------------------------------------------------------------------------")

class DISHES():
    def __init__(self):
        print("self hashcode:",self)
        self.name= "noodles"
        self.price= "300 \u20B9"
        self.quantity = "1 plate"
        self.ratings = "5 \u2605"
        self.catagoryofdish = "chinese"

dish = DISHES()#object creation
print("dish hashcode:",dish)
print("----------------------------------------------------------------------------------")
print(" \u2728 DISHES \u2728 \n")
print("NAME:",dish.name,"\n","Price:",dish.price,"\n","Quantity:",dish.quantity,"\n","Ratings:",dish.ratings,"\n","Catagory of dish:",dish.catagoryofdish,"\n")


