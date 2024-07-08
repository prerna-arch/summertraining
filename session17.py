"""

"""
#1D List
#indexing
#         0  1  2
#        -3 -2 -1
my_data=[10,20,30]

#2D List(list of lists)
numbers = [

          [10,20,30], #0 -3
          [30,40,50], #1  -2     #indexing
          [60,70,80]  #2  -1
]

#3D LIST of list of lists
#indexing
large_data = [
        [

          [10,20,30], 
          [30,40,50],                       #0      -2
          [60,70,80] 
        ],
        [
          [90,100,110], 
          [120,130,140],                      #1       -1
          [150,160,170]  
        ]

]






print(my_data[0])
print(my_data[-1])
print(len(my_data))

print(numbers[0])
print(numbers[-1])
print(len(numbers))

print(large_data[0])
print(large_data[-1])
print(len(large_data))


print(large_data[1][0][0])
print(large_data[-1][-3][-3])

#STRING
name="johns cafe"
name='john\'s cafe'
name="""
johns cafe


"""


print(name)


#4 concatenation
data1= [10,20,30]
data2= [40,50,60]
data3= data1 + data2 
print(data3)

#5 Multiplicity
data4= data1 *2
print(data4)

prices=[100,500,700,300]
prices1=prices *2
print(prices1) 

#6 Membership testing
print(10 in prices)  #false
print(10 not in prices) #true

quote="search the candle than cursing the darkness"
print(quote[5])


#SET
"""
#indexing not working
numbers={10,20,30,40}
print(numbers[0])

#slicing not working
print(numbers[1:3])

#cancatenatiom not working
num={2,3,4}
num2=numbers + num
print(num2)

#multiplicity not working
num3=num*2
print(num*3)

#membership testing
num={2,3,4}
print(10 in num)
print(10 not in num)
"""
#Dictionary
#indexing  not working as it has keys ,it works on keys
names={1:"sam",2: "yuvi"}
print(names[1])

#slicing not working
#print(names[1:2])

#concatenatin not working
#names2={3:"son"}
#names3=names + names2
#print(names3)

#membership testing is working on keys

