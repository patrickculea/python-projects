num = int(input("please give me a number value for the numb variable, and I will tell you your chosen value in binary form."))
s = ""
while num > 0:
    r= num % 2
    s = str(r)+s
    num = num // 2

int(s)
print(s)
