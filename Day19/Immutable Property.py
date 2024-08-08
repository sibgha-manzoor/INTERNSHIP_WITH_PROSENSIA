fruit = ('apple', 'banana', 'cherry')
try:
    fruit[1] = 'cherry'
except TypeError as e:
    print("Immutable Property of tuple")