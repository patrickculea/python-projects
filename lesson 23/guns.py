class weapons:
    def __init__(self,name,firerate,damage,mobility,explosion,range):
        self.name = name
        self.firerate = firerate
        self.damage = damage
        self.mobility = mobility
        self.explosion = explosion
        self.range = range
    def display_info(self):
        print(f"The name of the weapon is {self.name} \nthe firerate is {self.firerate} \nthe damage is {self.damage}\nthe mobility is{self.mobility}\nthe statement: it causes explosions is {self.explosion}\nThe range is {self.range} metres")
class guns(weapons):
    def __init__(self,name,firerate,damage,mobility,explosion,range,mag_size,):
        super().__init__(name,firerate,damage,mobility,explosion,range)
        self.mag_size = mag_size

    def auto(self):
        autonomy = self.mag_size / self.firerate
        return autonomy
    

    def display_info(self,auto):
        super().display_info()
        print(f"It has a magazine size of: {self.mag_size}")
        print("it has an autonomy of ",auto(self),"seconds.")

class tanks(weapons):
    def __init__(self,name,firerate,damage,mobility,explosion,range,durability):
        super().__init__(name,firerate,damage,mobility,explosion,range)
        self.durability = durability
    def display_info(self):
        super().display_info()
        print(f"The durability of the is tank is {self.durability}")

gun_1 = guns("desert_eagle",100,200,"high",False,100,8)
gun_2 = guns("acr",700,50,"medium",False,120,30)
gun_3 = guns("NTW-20",15,2000,"Very low",False,2300,3)
tank_1 = tanks("T-54","4",5000,"very high",True,6500,"Very high")
my_weapons=[gun_1,gun_2,gun_3,tank_1]
my_guns = [gun_1,gun_2,gun_3]
for x in my_guns:
    x.display_info(guns.auto)

tank_1.display_info()
    




        
        