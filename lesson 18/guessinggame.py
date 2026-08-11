import random
game = True
num = str(random.randint(1,10))
print("Lets play a game.")
print("I will generate a random integer number inbetween and including 1 and 10. You have to guess what it is")
attempt = 0
while game:
    attempt += 1
    guess =input(f"Attempt{attempt}:")
    if guess == num:
        print("Right answer.")
        break
    elif guess < num:
        print("Your number is lower than the right number.")
    else:
        print("Your number is larger than the right number.")
            


