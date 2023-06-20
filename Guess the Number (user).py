import random

def computer_guess(x): 
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low
            
        print (f"Is it {guess}?")
        print ("Type 'c' to correct.")
        print ("Type 'h' to too high.")
        print ("Type 'l' to too low ")
        feedback = input("-> ").lower()
        if (feedback == "h"):
            high = guess - 1
        if(feedback == "l"):
            low = guess + 1

    print(f"Yaay! The computer guessed your number, {guess}, correctly! ;)")

limit = int(input("Tell the limit: "))
computer_guess(limit)