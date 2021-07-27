import random 
print("Guessing Game")
Number=random.randint(1,9)
chances=0
print("Guess A Number Between 1 and 9")

while chances<5:
    guess=int(input("Guess The Number"))
    if(guess==Number):
        print("You Have Guessed The Correct Number")
        break
    elif(guess<Number):
        print("You Have Guessed A Number Lower Than The Correct One")
    elif(guess>Number):
        print("You Have Guessed A Number Higher Than The Correct One")
    else:
        print("You Have Guessed The Wrong Number")
    chances=chances+1

if(chances==5):
    print("You Have Used All Your Chances")
    print("You Lost")
    print("The Correct Number is ",Number)
