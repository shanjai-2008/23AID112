secret = 7

guess = None
while guess != secret:
    guess = int(input("Guess the number: "))
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")

print("Correct! You guessed it 🎉")
