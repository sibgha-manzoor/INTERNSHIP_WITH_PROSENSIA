tuple1 = (1,2,3)
list1 = [1,2,3]

try:
    tuple1.append(4)
except:
    print("Error: 'tuple' object has no attribute 'append'")

list1.append(4)

print(list1)
print(tuple1)