import sys
class bomba:
    def __init__(self,colours,remtime,):

        self.colours = colours
        self.remtime = remtime
    def initial_meth(self):
        while True:
            print("Your mission is to detonate the bomb in 60 seconds")
            start = input("input start to start the mission")
            if start == "start":
            
                return True
                break
                
            else:
                print("error, you didnt type in start, please try again")
                continue
    def detonation1(self):
        import random
        import time
        ticking = time.time()
        w1 = random.choice(self.colours)
        self.colours.remove(w1)

        w2 = random.choice(self.colours)
        self.colours.remove(w2)

        w3 = random.choice(self.colours)
        self.colours.remove(w3)

        w4 = random.choice(self.colours)
        self.colours.remove(w4)

        w5 = random.choice(self.colours)
        self.colours.remove(w5)

        order = f"{w1} {w2} {w3} {w4} {w5}"
        bomb =""
        ticking =time.time()

        print("There are 5 wires, 1 yellow, 1 orange, 1 green, 1 red, 1blue")

        
        while bomb != "defused":
            if time.time()-ticking >= self.remtime:
                print("BOOOOOM")
                sys.exit()
            cut = input("What is the order?")
            if cut == order:
                bomb = "defused"
        
                print("You have succesfully defused the bomb!")
                sys.exit()


b1 = bomba(["green","blue","orange","red","yellow"],60)
if b1.initial_meth():
    b1.detonation1()



        
