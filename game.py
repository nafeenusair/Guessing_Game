import random

low = 1
high = 10
guess = 3
numbers = random.randint(low, high)

print("You have 3 chances to guess the number from 1 to 10")
print()
while guess != 0:
    chance = 1
    print(f"You have {guess} chances left")
    ans = int(input(f"Enter your #{chance} guess: "))

    if ans is not numbers:
        print("Wrong! Try Again...")
        print()
        guess -= 1
    else:
        print("Correct! You won")
        break

if guess == 0:
    print(f"You failed to guess the number.\nThe number was {numbers}")
