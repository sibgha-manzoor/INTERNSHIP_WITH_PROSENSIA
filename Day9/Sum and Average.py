sum = 0
count = 0

while True:
    i = input("Enter number:")
    if i == "done":
        break
    i = int (i)
    sum += i
    count += 1 

print(sum)
if count > 0:
    avg = sum / count
    print(avg)
else:
    print("No data entered")