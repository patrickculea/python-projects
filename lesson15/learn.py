def sum1(a,b):
    return a + b

def sum2(c,d):
    return c+d

def times(a,b,c,d):
    return a * b * c * d

a = int(input("Please introduce 4 variables, a ,b ,c and d."))
b = int(input("please b"))
c = int(input("please c"))
d = int(input("please d"))

op = input("Please input the minus symbol if you would like me to preform :(a + b) - (c + d), or input the plus symbol(+), if you would like me to preform:(a + b) + (c + d), If you would like me to multiply all of the numbers press x, and lastly, if you would like me to preform:(a+b) / (c+d), press /")

if op == "+":
    print(sum1(a,b) + sum2(c,d))

if op == "-":
    print((sum1(a,b)) - (sum2(c,d)))

if op == "x":
    print(times(a,b,c,d))

if op == "/":
    print((sum1(a,b)) / ((sum2(c,d))))
