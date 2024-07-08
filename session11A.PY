from session10F import customer
#file handling
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
print("-------------------WELCOME TO CUSTOMER MANAGEMENT SYSTEM-----------------------------")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")

while True:

    print("1.Add customer")
    print("2.view customer")
    print("3.Quit")

    choice = int(input("Enter your choice:"))
    print("You selected:",choice)

    if choice==1:
       file =open("customer.csv","a") 
       customer1  = customer()
       customer1.add_customer_details()
       customer1.show()


       data=customer1.to_csv()
       file.write(data)
       print("data written:",data)

    elif choice==2:
        file=open("customer.csv","r")
        lines =file.readlines()
        for line in lines:
            print(line)


    elif choice==3:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
        print("-------------------THANKYOU-----------------------------")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
        file.close()
        break







    
    






