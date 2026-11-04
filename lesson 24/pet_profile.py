class pet:
    print("The program has begun.")
pet_object=pet()
class petprof:
    category = pet
    def __init__(self,name,animal_type,age,fav_food):
        self.fav_food = fav_food
        self.name=name
        self.animal_type=animal_type
        self.age=age

pet1=petprof("Ben","Golden retriever","4","treats")
pet2 =petprof("Lola","Praying Mantis","2","worms")
my_animals = [pet1,pet2]
    
for x in my_animals:
    print(f"Their name is {x.name}\nTheir species is {x.animal_type}\nThey are {x.age} years old,\nAnd their favourite food is {x.fav_food}.")

