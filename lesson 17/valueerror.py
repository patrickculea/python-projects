while True:
    try:
        num = int(input("Please give me an integer value. I will print its value doubled"))
        print(num * 2)
        break
    except ValueError as elephant:
        print(elephant)
        print("I told you to give me an integer value")
        
    finally:
        print("the program has finished.")



