units = int(input("hpow many units of electricity have you used in the last month?"))
amount = 0
tax = 0
if units < 50:
    amount =units * 2.60
    tax = 25

elif (units >= 50 and units < 100):
    amount =130 + (units - 50) * 3.25
    tax = 35
    
elif ( units <= 200 and units > 100 ):
    amount = 130 + 162.5 + (units - 100) * 5.26
    tax = 45

else:
    amount =130 + 162.5 + 526 + (units - 200) * 8.45
    tax = 75

total = amount + tax
print(f"You will have to pay {total} for how many units you have used in the last month.")


