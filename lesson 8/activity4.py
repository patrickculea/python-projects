# 1) Take three integer inputs from the user and store them in `a`, `b`, and `c`.
a = int(input("tell me value 1:"))
b = int(input("tell me value 2:"))
c = int(input("tell me value 3:"))
# 2) Calculate the average of `a`, `b`, and `c`:
avg = (a + b + c) / 3
# - Print `avg`
print(f"the average of your 3 values is {avg}")
# 3) Compare `avg` with `a`, `b`, and `c` using if–elif:
if avg > a and avg > b and avg > c:
# - If `avg` is greater than all three numbers, print that it is higher than `a`, `b`, and `c`.
    print(f"the average({avg})is larger than {a}, {b}, and {c}")
# - Else if `avg` is greater than `a` and `b`, print that it is higher than `a` and `b`.
elif avg > a and avg > b:
    print(f"the average{avg} is grater than {a} and {b}")
    
# - Else if `avg` is greater than `a` and `c`, print that it is higher than `a` and `c`.
elif avg > a and avg > c:
    print(f"the average {avg} is larger than {a} and {c}")
# - Else if `avg` is greater than `b` and `c`, print that it is higher than `b` and `c`.
elif avg  > b and avg > c:
    print(f" the average {avg} is bigger than {b} and {c}")
# - Else if `avg` is greater than only `a`, print that it is just higher than `a`.
elif avg > a:
    print(f"the average {avg} is larger than {a}")
# - Else if `avg` is greater than only `b`, print that it is just higher than `b`.
elif avg > b:
    print(f"the average {avg} is greater than only {b}")
# - Else if `avg` is greater than only `c`, print that it is just higher than `c`.
elif avg > c:
    print(f"the average {avg} is only greater than {c}")
# 4) If none of the above conditions match, print "invalid input".
else:
    print("invalid inputs")