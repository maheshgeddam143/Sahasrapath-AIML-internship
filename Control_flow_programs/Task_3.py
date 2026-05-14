secret_number = 7

guess = int(input("Guess the number: "))

while guess != secret_number:

    if guess > secret_number:
        print("Too High")
    else:
        print("Too Low")

    guess = int(input("Guess again: "))

print("You Won")
