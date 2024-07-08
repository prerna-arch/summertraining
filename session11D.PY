
#read mode in file handling
file = open("customer1.csv","r")
# data = file.read()

lines = file.readlines()

print("file data:")
print(lines)

for i in range(len(lines)):
    print(lines[i])