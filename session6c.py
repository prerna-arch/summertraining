def square_of_numbers(nums):
    print("1.nums is:",nums,id(nums))#10
    for idx in range(0,len(nums)):
        nums[idx] = nums[idx] * num[idx]
    
    print("2.num is:",nums,id(nums))#100
    return
number = [10,20,30,40,50]
print("number is :", number ,id(number))#1
square_of_numbers(number)
print("number is :", number,id(number))#10