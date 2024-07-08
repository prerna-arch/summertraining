#explore dictiornary/map/json
#keys can not be duplicate 
my_data={
        101:"john",
        201:"jennie",
        501:"sia",
        99:"joe",
        25:"joy",

}
"""
my_data = {
     "jo": "John",
    "je": "Jennie",
    "si": "Sia",
     "ji": "Joe",
     "ki": "Kim"
 }"""

print("my_data")
print(my_data)

print("my_data:",my_data)
print("len  is",len(my_data))
print("sum  is",sum(my_data))
print("min is",min(my_data))
print("maxis",max(my_data))

print(my_data[25])
print(my_data.get(25))


my_data.pop(25)
#del my_data[25]
print(my_data)

my_data[99]="harry"
print(my_data)

attendence=["june","july","aug"]
college_attendence={}.fromkeys(attendence,100)
print(college_attendence)


items=list(my_data.items())
values=list(my_data.values())

print(items)
print(values)

for item in my_data.items():
    print(item)

for value in my_data.values():
    print(value)
    
    