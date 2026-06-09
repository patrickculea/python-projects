num = int(input("please give me a whole number and i will tell you if it is an armstrong number."))
sum =0
temp = num
while temp > 0:
    digit =temp % 10
    sum += digit**3
    #print(sum)
    print(temp)
    temp //= 10

if num == sum:
    print("the number you gave me is an armstrong number.")
else:
    print("the number you gave me is not an armstrong number.")

