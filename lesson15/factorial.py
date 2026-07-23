
def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return(n * factorial(n-1))

n =int(input("Please introduce a number, I will find its factorial"))
method =input("Press l if you want me to find its factorial value using a loop, or press r if you want me to find it using recursion.")

def factoriall(n,tot=1):
    for i in range(1,n+1):
        tot *= i
    print(tot)
            

if method == "l":
    factoriall(n)
else:
    print(factorial(n))




    

        
