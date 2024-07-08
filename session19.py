numbers = list(range(10,101,10))
print("numbers is:",numbers)
print("numbers type  is:",type(numbers))
#duplicay and add numbers in list is possible

numbers.append(99)
numbers.append(12)
numbers.append(15)

print("numbers is",numbers)

print("len  is",len(numbers))
print("sum  is",sum(numbers))
print("min is",min(numbers))
print("maxis",max(numbers))
print("avg is",sum(numbers)/len(numbers))

result = list(reversed(numbers))
print("result is:",result)


# HW: reverse the below list using operators/for/if else/indexing etc...
#       0    1   2  3   4   5
data = [10, 20, 30, 40, 50, 30]
# data1 = []

# for idx in range(len(data)-1, -1, -1):
#     print(data[idx])
#     data1.append(data[idx])

# print(data1)

data=[10,20,30,40,50]
idx = data.index(40)
print("idx is:",idx)

result = data.count(30)
print("result is:",result)

#counting without inbuilt function
c=0
for idx in range(len(data)):
    if data[idx] == 30:
        c+=1
print("c is",c)


data=[10,5,12,16]
names=["john","Abel","sia","jennie"]

data.sort()
print("data is",data)
#hw  find how to sort in reverse order usimg the same sort function

names.sort()
print("name is",names)#sort acc to ascii codes

print(min(names))
print(max(names))

data=[10,5,12,16 ,30,30]
names.remove("sia")
data.remove(30)
print("name is",names)
print("data is",data)


data=[10,20,30,40,50]
data.pop()
print("data after pop:",data)
data.pop(0)
print("data after pop:",data)

data.clear()
print("clear:",data)

data=[10,20,30,40,50]
data.append(99)
data.insert(2,77) # insert 77 at 2nd index
data.insert(-1,88)# it will skip one position and then add in list
print("data is",data)


# del data[1]
# del data[1:4]
#TUPLE
numbers=(10,20,30,40,50)
print("numbers is:",numbers)
print("numbers type  is:",type(numbers))



#Append is not working in tuple
"""
numbers.append(99)
numbers.append(12)
numbers.append(15)
print("numbers is:",numbers)"""
#inserton is not working in tuple
"""
numbers.insert(2,77) # insert 77 at 2nd index
numbers.insert(-1,88)# it will skip one position and then add in list
print("numbers is",numbers)"""

#below all are working
print("len  is",len(numbers))
print("sum  is",sum(numbers))
print("min is",min(numbers))
print("maxis",max(numbers))
print("avg is",sum(numbers)/len(numbers))


#reversing is working on tuple
result = tuple(reversed(numbers))
print("result is:",result)

idx = numbers.index(10)
print("idx is:",idx)

result = numbers.count(30)
print("result is:",result)

#sorting is not working in tuple

data=(10,5,12,16)
names=("john","Abel","sia","jennie")
"""
data.sort()
print("data is",data)
names.sort()
print("name is",names)"""

print(min(names))
print(max(names))

# remove is not working on tuple
"""
names.remove("sia")
data.remove(5)
print("name is",names)
print("data is",data)
"""
#pop is not working on tuple
"""
data=(10,20,30,40,50)
data.pop()
print("data after pop:",data)
data.pop(0)
print("data after pop:",data)
"""
#clear is not working on tuple
"""
data=(10,20,30,40,50)
data.clear()
print("clear:",data)
"""
