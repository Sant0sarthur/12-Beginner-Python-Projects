import random 

def guess(x):
    random_number = random.randint(1, x)
    gues = 0
    while gues != random_number:
        gues = int(input(f"Guess a number between 1 and {x}: "))
        if (gues < 1) or (gues > x):
            print("Please, type a valid number.")
        else:
            if gues < random_number:
                print("Sorry, guess again. Too low. :(")
            elif gues > random_number:
                print("Sorry, guess again. Too high. :(")

    print(f"Yay, congrats. You have guessed the number {random_number} correctly! :)")    

limit = int(input("Tell the lmit: "))
guess(limit)