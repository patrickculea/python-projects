class agent():
    def __init__(self,name,health,car):
        self.name = name
        self.health = health
        self.car = car

    def player_info(self):
            print("Welcome",self.name)
            print("Your health:",self.health)
            print("Your car choice:",self.car)

spy =agent("James Bond",100,"Jaguar")  
villian =agent("John Jimmothy",70,"Tesla")

spy.player_info()
villian.player_info()
