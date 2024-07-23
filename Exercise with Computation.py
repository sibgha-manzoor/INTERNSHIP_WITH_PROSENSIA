try:
    hour = int(input("Enter Hours worked: "))
    rate = int(input("Enter Rate: "))
except:
    print("Invalid input")
    hour = -1
    rate = -1
if hour >= 0 and rate >= 0:
    if hour > 40:
        nrate = 1.5 * rate
        pay = 40 * rate + (hour - 40) * nrate
    else:
        pay = hour * rate
        print(pay)
else:
    print("Calculation cannot proceed due to invalid input.")
