
#elevator problem
floors = 10
floor  = 0
floor_to_go = int(input("enter floor number to go"))
"""
while floor <= floors: this is infinite loop ,example whatsappp,instagram
    print("at floor number:",floor)
         
         
    if floor_to_go == floor:
        print("you have reached at floor:",floor)
        break
    floor+=1

"""
for floor in range(0,11):
    print("At floor number:",floor)
    
    if floor_to_go == floor:
        print("you have reached :",floor)
        break
    


