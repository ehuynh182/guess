import random

print("Hello there! \nWhat is your name?")
name = input()

print("Hello " + name + ", I am thinking of a number between 1 and 20. Take a guess!")
secretNumber = random.randint(1,20)

print("Debug - secretNumber: " + str(secretNumber))

for guessTaken in range(1, 7):
    print('Take a guess:')
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low! Try again!")  

    if guess > secretNumber:
        print("Your guess is too high! Try again!")

    if guess == secretNumber:
        print("Good Job " + name + "! You guessed correct!")
        break

    else:
        print("Nope, the correct guess is " + str(secretNumber))