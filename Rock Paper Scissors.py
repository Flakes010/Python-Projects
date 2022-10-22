import random
print(("-" * 25) + "\nRock, Paper, Scissors\n" + ("-" * 25))

users_score = 0
computers_score = 0
gameVariables = [1,2,3]
while True:
    print("\n1)Rock\n2)Paper\n3)Scissors\n")
    users_choice = int(input("Please select your choice: "))
    computers_choice = random.choice(gameVariables)

    if users_choice == 1:
        if computers_choice == 1:
            print("Computer's choice: Rock, Scoreless!")
        elif computers_choice == 2:
            print("Computer's choice: Paper, Computer won!")
            computers_score += 10
        elif computers_choice == 3:
            print("Computer's choice: Scissors, You won!")
            users_score += 10

    elif users_choice == 2:
        if computers_choice == 1:
            print("Computer's choice: Rock, You won!")
            users_score += 10
        elif computers_choice == 2:
            print("Computer's choice: Paper, Scoreless!")
        elif computers_choice == 3:
            print("Computer's choice: Scissors, You lost!")
            computers_score += 10

    elif users_choice == 3:
        if computers_choice == 1:
            print("Computer's choice: Rock, You lost!")
            computers_score += 10
        elif computers_choice == 2:
            print("Computer's choice: Paper, You won!")
            users_score += 10
        elif computers_choice == 3:
            print("Computer's choice: Scissors, Scoreless!")

    if computers_score < users_score:
        print("\nYour Score is {}\nComputer's Score is {}\nYou are winning!".format(users_score, computers_score))
    elif computers_score > users_score:
        print("\nYour Score is {}\nComputer's Score is {}\nComputer is winning!".format(users_score, computers_score))
    elif computers_score == users_score:
        print("\nYour Score is {}\nComputer's Score is {}\nTie!\n".format(users_score, computers_score))

    Exit = int(input("\nDo you want to exit?\n1 = Yes, 2 = No\n=>"))
    if Exit == 1:
        break
    elif Exit == 2:
        continue
