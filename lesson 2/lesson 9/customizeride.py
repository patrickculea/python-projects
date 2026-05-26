print("Select your ride.")
print("1. bike")
print("2. car")
choice = int(input("1 or 2?"))
if choice == 1:
    print (" you have chosen bike")
    print("which type of bike?")
    print("1 = scooty")
    print("2 = scooter")
    choice2 = int(input("1 or 2"))
    if choice2 == 1:
        print("you have chosen a scooty")
    else:
        print("you have chosen scooter")

if choice == 2:
    print("you have chosen to use a car")
    print("1. Sedan")
    print("2. Xuv")
    choice2 = int(input("1 or 2?"))
    if choice2 == 1:
        print("You have chosen to drive a Sedan car.")
    else:
        print("you have chosen to drive a Xuv car.")


