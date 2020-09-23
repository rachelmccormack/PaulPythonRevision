number = 6

def guessCheck():
    guess = int(input("guess a number: "))
    if (guess == number):
        print("congrats")
    else:
        print("Sorry, guess again")
        guessCheck()

guessCheck()
