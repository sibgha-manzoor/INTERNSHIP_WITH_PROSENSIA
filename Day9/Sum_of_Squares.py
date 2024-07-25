num = int(input("Enter a natural number: "))
sum_of_squares = 0
i = 1
while i < num:
    sum_of_squares += i * i
    i += 1
print(f"The sum of the squares of the first {num} natural numbers is {sum_of_squares}.")
