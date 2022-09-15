import time


score = 0
print("-----Welcome to Quiz Game!-----\nFor each true answer you'll get 1 point and at the end you are going to see your score!\n")

firstquestion = input("What is the Capital City of Turkey: ")
if firstquestion.lower() == 'ankara':
    score += 1
    print("\nTrue!\nYour currently score: {}".format(score))
else:
    print("\nFalse! The correct answer would be 'Ankara'!\nYour current score: {}".format(score))
time.sleep(1)

secondquestion = input("\nWhat is the Capital City of Germany: ")
if secondquestion.lower() == 'berlin':
    score += 1
    print("\nTrue!\nYour currently score: {}".format(score))
else:
    print("\nFalse! The correct answer would be 'Berlin'!\nYour current score: {}".format(score))
time.sleep(1)

thirdquestion = input("\nWhat is the Capital City of England: ")
if thirdquestion.lower() == 'london':
    score += 1
    print("\nTrue!\nYour currently score: {}".format(score))
else:
    print("\nFalse! The correct answer would be 'London'!\nYour current score: {}".format(score))
time.sleep(1)

print("\nThe Game is finished, your score is {}".format(score))
