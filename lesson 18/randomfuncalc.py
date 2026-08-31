import random
import math
luckynum =random.randint(1,10)
print(luckynum)
fun_choices = ["skiing", "snowboarding", "checkers", "ninemesmorris", "chess", "sudoku", "meowdoku"]
fun_activity =random.choice(fun_choices)
print(f"Your chosen fun activity is:{fun_activity}.")
secret_num =random.randint(1,5)
while True:
    guess =int(input("Please guess what my random number is (from 1 to 5)"))
    if guess == secret_num:
        print("Congratulations, you guessed my random number!")
        break
    else:
        print(f"{guess} is not my lucky number. Please try again")
        continue

round_up = float(input("Please give me a decimal number to round up"))
print(math.ceil(round_up))

round_down =float(input("Please give me a decimal number to round down."))
print(math.floor(round_down))

x = int(input("Please give me 2 integer numbers. I will copy the sign of the second number on to the first"))
y = int(input(""))
print(math.copysign(x,y))

fab = float(input("Please give me a decimal value. I will return its absolute value."))
print(math.fabs(fab))

g = int(input("Please give me 2 integer numbers. I will tel you their gcd, (Greatest common divisor.)"))
c = int(input(""))
print(math.gcd(g,c))




    

