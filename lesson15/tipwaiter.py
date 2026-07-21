"""Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay."""
def total_calc(bill_amount,tip_perc):
    tip_perc /= 100
    total = bill_amount *(1 + tip_perc)
    print(f"The total amount you have to pay including the tip percentage is {total} Pounds.")

total_calc(150,20)