flag = False
while not flag:
    try:
        num = int(input("Please give me an integer value which is not 0."))
        if num % 2 == 1:
            print("Bye")
        if num % 2 == 0:
            print("You have finally Given me an even number and the code will stop repeating.")#
            flag = True
    except ValueError:
        print("I told you to give me an integer value. Please try again.")
        continue




