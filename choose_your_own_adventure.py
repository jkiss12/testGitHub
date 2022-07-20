name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go "
               "left or right. Which way you would like to go? ")
answer.lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim "
                   "across. (Type walk/swim): ")
    if answer == "swim":
        print("You swam across and were eaten by an alligator. ")
    elif answer == "walk":
        print("You walked for many miles, run out of water and you lost the game.")
    else:
        print("Not a valid option!, You lose!")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it"
                   "or head back? (Type cross/back): ")
    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (Type yes/no): ")
        if answer == "yes":
            print("You talked to the stranger and the give you the advice. You WIN!!! ")
        elif answer == "no":
            print("You missed your life opportunity and you lose!")
        else:
            print("Not a valid option!, You lose!")
    elif answer == "back":
        print("You go back and loose.")
    else:
        print("Not a valid option!, You lose!")
else:
    print("Not a valid option!, You lose!")

print("Thank you for trying", name)