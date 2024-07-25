num = 17
i = 0
while i < 10:
    print("Guess the number(1-50):")
    guess = int(input())
    if guess == num:
        print("You win")
        break
    else:
        print("Try again")
    i += 1
if guess != num:
    print("You lose")