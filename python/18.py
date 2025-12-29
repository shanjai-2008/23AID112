secret = 7
print("The secret number is between 1 to 100")
guess = None
while guess != secret:
    guess = int(input("Guess the number: "))
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")

print("Correct! You guessed it")
