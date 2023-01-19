import random
from utils import get_user_number

# generate a random number between 1 and 100
number = random.randint(1, 100)

# initialize the number of guesses
num_guesses = 0

# prompt the user to guess the number
guess = int(input("Guess a number between 1 and 100: "))

# keep prompting the user until they guess the number
while guess != number:
    if guess > number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")
    num_guesses += 1
    guess = get_user_number("Guess a number between 1 and 100: ")

# print a congratulatory message
print("Congratulations! You guessed the number in " + str(num_guesses) + " guesses.")
print()
print("Something to think about: what is the best strategy to win?")
