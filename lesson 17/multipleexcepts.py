try:
    print("Please give me two numbers. I will divide the second one by the first.")
    num1 = int(input("Number 1= "))
    num2 = int(input("Number 2= "))
except ZeroDivisionError as e1:
    print(e1)
except ValueError as e2:
    print(e2)
except NameError as e3:
    print(e3)
except:
    print("Wrong input!")

else:
    print("No exceptions.")

finally:
    print(f"the result is {num1 / num2}")
    print("This line of code will execute no matter what.")
