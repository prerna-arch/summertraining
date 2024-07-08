from session15 import Customer
from session15A import Database
from  tabulate   import tabulate 
def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("WELCOME TO CUSTOMER MANAGEMENT APP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     
    db=Database()

    while True:
        print("1:Add New customer")
        print("2:Update existing  customer")
        print("3:Delete existing customer")
        print("4:view customer by phone")
        print("5:view customer by cid")
        print("6:view all customer")
        print("0:Quit app")

        choice=int(input("enter your choice:"))

        if choice == 1:
            customer = Customer()
            customer.add_customer_details()
            sql="insert into Customer values(null,'{name}','{phone}','{email}',{age},'{gender}','{created_on}')".format_map(vars(customer))
            db.write(sql)
            print("[cms app]",customer.name,"saved in database")
        elif choice == 2:

            cid=int(input("Enter the customer cid to update the customer:"))
            sql="select * from Customer where cid={}".format(cid)
            rows= db.read(sql)
            print(rows)
            customer = Customer(cid=rows[0][0],name=rows[0][1],phone=rows[0][2],email=rows[0][3],age=rows[0][4],gender=rows[0][5])
            #columns =["cid","name","phone","email","age","gender","created_on"]
            #print(tabulate(rows,headers=columns,tablefmt='grid'))
            print("customer to update....")
            customer.show()      
            customer.update_customer_details()    

            sql="update customer set name='{name}',phone='{phone}',email='{email}',age={age},gender='{gender}',created_on='{created_on}' where cid={cid}".format_map(vars(customer))
            db.write(sql)
            customer.show()  

        elif choice == 3:
            cid=int(input("Enter the customer id"))
            sql="delete from Customer where cid={}".format(cid)
            ask = input("Are you sure to delete ? (yes/no)")
            if ask== "yes":

              db.write(sql)
              print("[cms app]",cid,"delete from database")
            else:
                print("delete operation skipped....")
        elif choice == 4:
            
            phone=(input("Enter the customer phone"))
            sql="select * from Customer where phone={}".format(phone)
            rows= db.read(sql)
            columns =["cid","name","phone","email","age","gender","created_on"]
            print(tabulate(rows,headers=columns,tablefmt='grid'))
            
        

        elif choice == 5:
            cid=int(input("Enter the customer cid"))
            sql="select * from Customer where cid={}".format(cid)
            rows= db.read(sql)
            columns =["cid","name","phone","email","age","gender","created_on"]
            print(tabulate(rows,headers=columns,tablefmt='grid'))
            
        elif choice == 6:
            sql="select * from Customer"
            #customers =db.read(sql) this customers are rows in db language
            rows =db.read(sql) 
            columns =["cid","name","phone","email","age","gender","created_on"]
            print(tabulate(rows,headers=columns,tablefmt='grid'))
            #for customer in customers:
             #  print(customer)

            
        elif choice == 0:
            break
        else:
            print("[cms app]inavlid choice")


if __name__=="__main__":
    main()