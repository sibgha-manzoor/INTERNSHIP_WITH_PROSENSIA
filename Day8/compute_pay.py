def compute_pay(hour,rate):
    if hour > 40:
        nrate = 1.5 * rate
        pay = 40 * rate + (hour - 40) * nrate
    else:
        pay = hour * rate
    return pay

result = compute_pay(45,10)
print(result)