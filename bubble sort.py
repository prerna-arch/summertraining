
number=[1,8,6,3]
print("THE UNSORTED LIST:",number)
for i in range(0,len(number)):
    for j in range(i+1,len(number)):

        if number[j]<number[i]:
            temp = number[i]
            number[i] = number[j]
            number[j] = temp

print("THE SORTED LIST IN ASCENDING ORDER:",number)
     
  

  
   

