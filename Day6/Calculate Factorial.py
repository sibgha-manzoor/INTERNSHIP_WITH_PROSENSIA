num = int(input("Enter a number: "))
factorial = 1
i = num
while i > 0:
 factorial *= i
 i = i-1
print("Factorial: ")
print(factorial)