def print_number(number):
    print(number)
    
    if number < 10:
     print_number(number+1)#function calling again and again

print_number(1)