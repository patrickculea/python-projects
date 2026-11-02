class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age

blu =parrot("blu",12)
woo = parrot("woo",3)
for i in (blu,woo):
    print(f"The species is {i.species}")
    print(f"The name is {i.name}")
    print(f"The age is {i.age}")