lower = int(input("please enter the lower range."))
upper = int(input("please input the upper range"))
print("I will tell you all prime numbers betweeen the two numbers you have entered.")
numbers = ""

for num in range(lower,upper + 1):
    if num > 1 :
        for i in range(2,num):
            if num % i == 0:
                break
            else:
                if numbers != str(num):
                 numbers += str(num)

print(numbers)

