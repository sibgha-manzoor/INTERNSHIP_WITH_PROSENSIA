num = int(input("Enter a Number: "))
if num > 0 and num % 2 == 0:
 print("Positive and even")
elif num > 0 and num % 2 == 1:
 print("Positive but odd")    
elif num < 0:
 print("Negative")
else :
 print("Zero")