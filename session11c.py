# append mode,file handling
name = input("Enter customer name:")
phone = input("Enter customer phone:")
email = input("Enter customer email:")

customer_details ="{},{},{} \n".format(name,phone,email)

file=open("customer1.csv","a")
file.write(customer_details)
print("customer data saved.....")
file.close()