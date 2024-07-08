#when you need to pass variable input to function(i.e 1 number or n numbers)
def add(*args):
    print(args)
    data = list(args)
    print(data)
    print(type(args))
    print(type(data))
    

add(10,20,30,40,50,"hi","hello","john")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")

def num(**kwargs):
    print(kwargs)
    print(type(kwargs))

num(a=10,b=20)




