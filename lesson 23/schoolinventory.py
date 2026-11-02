items =["pens","pencils","rulers","books"]
prices = [0.20,0.15,0.25,5]
choice =input("Would you like a 10 percent off discount on all the items that cost more than 50 pounds? y for yes n for no")
quantities = [300,200,100,400]

all_price = 0
if choice == "y":
    rlinventory_calc =list(map(lambda a,b: a*b ,prices,quantities))
    tot_price = rlinventory_calc
    discounted_prices=[price * 0.9 if price > 50 else price for price in tot_price]
    inventory_calc =list(map(lambda a,b: a*b , discounted_prices,quantities))
    print(f"The discounted prices are {discounted_prices}")
    print(f"The normal total price on the other hand are {tot_price}.")

    for items,prices,quantites,tot in zip(items,prices,quantities,discounted_prices): 
        print(f"We need{quantites}, {items}.")
        print(f"Each one will cost {prices} GBP")
        print(f"If we buy how many we need, it will cost us {tot} GBP, with discounts applied.")
        all_price += tot

    print(f"The total price to buy absolutely everything we need is {all_price}GBP, with discounts applied")

else:
    inventory_calc =list(map(lambda a,b: a*b , prices,quantities))
    tot_price = inventory_calc
    
    for items,prices,quantites,tot in zip(items,prices,quantities,tot_price):
        print(f"We need{quantites}, {items}.")
        print(f"Each one will cost {prices} GBP")
        print(f"If we buy how many we need, it will cost us {tot} GBP.")
        all_price += tot

    print(f"The total price to buy absolutely everything we need is {all_price}.")

    
