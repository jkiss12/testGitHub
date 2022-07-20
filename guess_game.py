# number_guessing

import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)    # casting into int

    if top_of_range <= 0:
        print("Please type a number greater then 0 ")
        quit()
else:
    print("Please type a number ")
    quit()

random_number = random.randint(0, top_of_range)

# keep asking for the guess
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)  # casting into int
    else:
        print("Please type a number ")
        continue

    if user_guess == random_number:
        print("You got it ")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You needed", guesses, "guesses")
print("Here are some random numbers to consider")
r = random.randrange(-5, 11)  # does not include the last number
print(r)
d = random.randint(-5, 11)          # does include the last number
print(d)