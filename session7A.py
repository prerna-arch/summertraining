def get_max(data,length):
    if length == 1:
        return data[0]
    else:
        previous = get_max(data,length-1)
        current = data[length-1]
        if previous > current:
            return previous
        else:
            return current


numbers = [10,20,30]#numbers,max belongs to main frame
max = get_max(numbers,len(numbers))
print("Max is:",max)

