def print_value(dictionary, key):
    if key in dictionary:
        print(dictionary[key])
    else:
        print("Key not found")

fruit = dict()
fruit['apple'] = 1
fruit['banana'] = 9
fruit['grapes'] = 5

print_value(fruit, 'banana')  
print_value(fruit, 'orange')  