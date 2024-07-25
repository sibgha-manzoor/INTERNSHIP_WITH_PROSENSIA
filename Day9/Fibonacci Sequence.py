num = int(input("Enter the number of Fibonacci numbers: "))
a = 0
b = 1
i = 0
print("Fibonacci sequence:")
while i < num:
    print(a, end=' ')
    a, b = b, a + b  
    i += 1