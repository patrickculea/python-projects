import time
import random
import sys
x = ["red","blue","yellow","orange","green"]
w1 = random.choice(x)
x.remove(w1)

w2 = random.choice(x)
x.remove(w2)

w3 = random.choice(x)
x.remove(w3)

w4 = random.choice(x)
x.remove(w4)

w5 = random.choice(x)
x.remove(w5)

order = f"{w1} {w2} {w3} {w4} {w5}"
bomb =""
ticking =time.time()
print(order)
print("There are 5 wires, 1 yellow, 1 orange, 1 green, 1 red, 1blue")


while bomb != "defused":
    if time.time()-ticking >= 60:
        print("BOOOOOM")
        sys.exit
    cut = input("What is the order?")
    if cut == order:
        bomb = "defused"
        
        print("You have succesfully defused the bomb!")
        sys.exit()





