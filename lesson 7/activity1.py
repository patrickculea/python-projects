# 1) Store the value 5 in `x`.
x =5
# 2) Check if the datatype of `x` is exactly `int` using the identity operator `is`.
if type(x) is int:
# - If it is an int, print "true"
    print("true")
# - Otherwise, print "false"
else:
    print("false")
# 3) Store the value 5.5 in `x`.
x =5.5
# 4) Check if the datatype of `x` is NOT `float` using `is not`.
if type(x) is not float:
# - If it is not a float, print "true"
    print("true")
# - Otherwise, print "false"
else:
    print("false")
# 5) Store the value 20 in `x` and 20 in `y`.
x =20
y =20
# 6) Check if `x` and `y` refer to the same object (same identity) using `is`.
if x is y:
# - If yes, print "x & y SAME identity"
    print("x and y have the same identity")
# 7) Change `y` to 30.
y =30
# 8) Check if `x` and `y` do NOT refer to the same object using `is not`.
if x is not y:
# - If yes, print "x & y have DIFFERENT identity"
    print("x and y have different identitys")
else:
    print("x and y stil have the same identity")