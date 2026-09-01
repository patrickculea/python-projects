import math
print("I will use the ceil and floor operator to round 23.56 up and down.")
num = 23.56
print("23.56 rounded up is:",math.ceil(23.56),"and rounded down its :",math.floor(num))
print("I will know take to integers from you. I will put the second numbers sign onto the first.")
x = int(input("x"))
y = int(input("y"))
print(math.copysign(x,y))
fab = 0

def fabmath():
    fab = float(input("Please give me a decimal number. I will print its absolute value"))
    print(math.fabs(fab))
    

fabmath()

fabmath()

print("The greatest common divisor of 24 and 56 is:",math.gcd(24,56))

