def multiply(a,b):
    return a + b

def division(a,b):
    return a / b

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

while True:
    op = str(input("Which operation would you like to preform?addition , multiplication , division , or subtraction?"))
    if op == "addition":
        break
    if op =="subtraction":
        break
    if op =="multiplication":
        break
    if op =="division":
        break
    if (op != "division" and op != "multiplication" and op != "addition" and op != "subtraction"):
        print("Invalid operation.")
        continue

try:
    a = int(input("Please give me  2 numbers. I will preform with them.",op, "for subtraction i will subtract the second integer from the first, and for division i will divide the second integer by the first.integer 1 = "))
    b =int(input("integer 2 ="))
    if op == "division":
        print(division(a,b))
    if op == "subtraction":
        print(subtraction(a,b))
    if op == "multiplication":
        print(multiply(a,b))
    if op == "addition":
        print(addition(a,b))
except TypeError as error1:
    print(error1)
except ZeroDivisionError as error2:
    print(error2)

