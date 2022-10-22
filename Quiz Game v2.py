score = 0
chance = 3
chance1 = 3
chance2 = 3
print("----- Welcome to Kadir Ihsan's Quiz Game -----")
print("We are going to ask you 3 questions. If you could answer all of them correctly, you would win!")
while True:
    firstquestion = input("What is the world's longest river called?\n>>>")
    if firstquestion.lower() == "nile":
        print("Correct!")
        score += 1
        break
    else:
        chance -= 1
        print("Wrong! You have only", chance,"Chance!")
        if chance == 0:
            print("You have not got chances anymore!")
            break

while True:
    secondquestion = input("Which planet is closest to Earth?\n>>>")
    if secondquestion.lower() == "venus":
        print("Correct!")
        break
    else:
        chance1 -= 1
        print("Wrong! You have only", chance1,"Chance!")
        if chance1 == 0:
            print("You have not got chances anymore!")
            break

while True:
    thirdquestion = input("Who is the author of the Harry Potter Series?\n>>>")
    if thirdquestion.lower() == "j.k. rowling":
        print("Correct!")
        break
    else:
        chance2 -= 1
        print("Wrong! You have only", chance2,"Chance!")
        if chance2 == 0:
            print("You have not got chances anymore!")
            break

print("\nGame is over, your score is {}".format(score))
