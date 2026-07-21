"""Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3"""
def cube(num):
    num = num ** 3
    print("The cube of the number is " ,num )

def three(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False
    
print(three(9))
print(three(4))
print(three(6))

