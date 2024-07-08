def add(num1,num2,num3):
    result = num1+num2+num3
    print("result is:{}".format(result))

#ways of executing function
#add(10,20,30)
add(num1=20,num2=10,num3=10)

#Default arguments/inputs
def square(num=5):
    result = num*num
    print("result is:{}".format(result))

square()
square(3)
square(num=9)


#def subtract(num1=20,num2):#throw error

def subtract(num1,num2=20):
    result=num1-num2
    print("subtract:",result)

subtract(num1=40)
    