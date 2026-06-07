num =int(input("give me a number base to power with n"))
n =int(input("give me a value to be n"))
ans=1
for i in range(1,n+1):
    ans = ans * num

print(ans)