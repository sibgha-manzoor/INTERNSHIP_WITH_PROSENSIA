year = int(input("Enter a Year: "))
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
         print("Year is a leap year.")
    else:
        print("Year is not a leap year.")
else:
    print("Year is not a leap year.")