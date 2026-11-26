class vehicle:
    def __init__(self,brand,max_speed):
        self.brand = brand
        self.max_speed = max_speed
    def show_details(self):
        print(f"The brand is: {self.brand}\nThe max speed is: {self.max_speed}")
class car(vehicle):
    def __init__(self,brand,max_speed,model,seats):
        self.model = model
        self.seats = seats
        super().__init__(brand,max_speed)
    def show_details(self):
        print(f"The car model is: {self.model}\nIt has {self.seats} seats.")
        super().show_details()
    def fuel_type(self,fuel):
        print(f"{self.model} uses {fuel}")

car1= car("aventador",180,"Lamporghini",2)
car1.show_details()
car1.fuel_type("petrol")
print("The statement -car is a subclass of vehicle- is",issubclass(car,vehicle))



    

    


            