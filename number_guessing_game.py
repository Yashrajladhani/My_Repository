import random
winnning_number = random.randint(1,30)
guess = 1
number = int(input("Guess a number between 1 and 30: "))
game_over = False
while not game_over:
    if number == winnning_number:
        print(f"You win, and you gussed this number in {guess} times")
        game_over = True
    else:
        if number < winnning_number:
            print("Too LOw")
        else:
            print("too high")
    guess +=1
    number = int(input("Guess Again: "))
