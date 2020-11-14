import random

random_number = random.randrange(1,20)
lives = 4

while lives > 0:
    guess = int(input("write an number between 1 to 20: "))
    if guess == random_number:
        print("Congrats, you are at last correct.")
        break
    elif guess < random_number:
        print('Think higher')
        lives -= 1 
    elif guess > random_number:
        print("don't think that far")
        lives -= 1 
else:
    print("GAME OVER, YOU LOST IN SUCH THE EASIEST GAME OF ALL TIME")