import random
import sys

credits = 10
spins = 0
bell = "\N{bell}"
orange = "\N{tangerine}"
grapes = "\N{grapes}"
banana = "\N{banana}"
cherries = "\N{cherries}"
lemon = "\N{lemon}"
watermelon = "\N{watermelon}"

symbols = [bell, orange, grapes, banana, cherries, lemon, watermelon]


def spin():
    global credits, spins

    x = random.choice(symbols)
    y = random.choice(symbols)
    z = random.choice(symbols)

    print(x, y, z)

    if x == y == z != cherries:
        credits += 4
        print("Well done, +4")
    
    elif x == y == z == cherries:
        credits += 6
        print("Damn! You got it, +6")

    elif x == y or y == z or x == z:
        credits += 1
        print("Great! +1")
    
    else:
        print("shit!")

    credits -= 1
    spins += 1


    print(f"You have currently {credits} credits!")


print(3*"\N{slot machine}" + " WELCOME TO SLOT MACHINE! " + 3*"\N{slot machine}")
print("You have all in all {} credits!".format(credits))
print("Your goal is to spin as much as possible. If 2 symbols match together, you'll get 1 credit more. If 3 symbols match, you'll get 4 credits more")
print("If you get the cherry in all three slots, you'll get 6 credits more!")

def main():
    global credits, spins

    while True:

        option = input("\nDo you want to spin(y/n): ")
        if option.lower() == "y":
            while credits > 0:
                spin()
                break
        elif option.lower() == "n":
            sys.exit()
        else:
            print("Please type 'y' for yes or 'n' for no!")
            continue

        if credits <= 0:
            print("Oh it seems like you don't have any credits more!\n")
            print(f"You reached {spins} spins!")

        if credits == 0:
            credits += 10
            spins -= spins

main()
