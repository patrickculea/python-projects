num=int(input("please input a number and I will count the digits."))
count = 0
while num !=0:
    num //= 10
    count += 1

print(f"your number has {count} digits.")

