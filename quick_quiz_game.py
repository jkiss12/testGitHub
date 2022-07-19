
print("Hi stranger!")
print("Welcome to the Quiz Game!")
score = 0
playing = input("Do you want to play? ")

if playing.lower() != "yes" or playing.lower() == "y":  # convert to lower case
    quit()
print("Let's play a game!")

answer = input("How many days are in January? ")
    if answer.lower() == "31":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

answer = input("What does RGB stand for? ")
    if answer.lower() == "red green blue":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

answer = input("How many days are in January? ")
    if answer.lower() == "31":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print("Your score is " + str(score))
print("Your got  " + str((score / 3) * 100) + "%.")