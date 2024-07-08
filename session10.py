def add(num1,num2):
    result = num1 + num2
    print("result is:{}".format(result))



print(hex(id(add)))
print("add:",add)
#add is a function and you will see the hash code of function
#execute add function
add(10,20)


#reference  copy operation
hello = add

hello(30,10)

#if you redefine the same fuction,the previous function will be removed from memory
#and new def will exist
def add(num1,num2,num3):
    result = num1 + num2+num3
    print("result is:{}".format(result))

print(hex(id(add)))
print("add:",add)


add(10,30,10)

    