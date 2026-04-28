numn =int(input("tell  me a number to be the numerator:"))
numd =int(input("tell me a number to be the denominator:"))
if numn % numd == 0:
    print(f"{numn} is divisible by {numd}")
else:
    print(f"{numn} is not divisible by {numd}")