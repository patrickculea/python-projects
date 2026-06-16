num = int(input("please input a number with at lest 4 digits and an even number of digits."))
numlen = len(str(num))
num = int(num)
product = 1
med1 = 1
med2 = 1
print(numlen)
t = numlen
if numlen % 2 == 0:
    t = int(numlen) // 2
    check = 0
    while num > 0:
        remainder = num % 10
        if check == numlen:
            med1 = remainder
        elif check == numlen - 1:
            med2 = remainder
            num = int(num // 10)
        product = med2 * med1

print(f"The product of your 2 middle numbers,{med1} and {med2}, is {product}")
print(med1)
print(med2)
        
    

