#file handling
quote = input("enter the data \n")
quote1 = input("enter the data \n")


file = open("data.txt","w")

#file = open("data.txt","a")
file.write(quote)
file.write(quote1)
#free memory resource once,you have used the file
file.close()

print("data written....")
