def calculate_change(total_inserted,price):
    change =total_inserted - price
    return change

price = 30
print("The ticket costs 30p. This machine only accepts 10,5, or 20 pence coins.")
total_inserted =0
coins_inserted = 0
while True:
    if total_inserted >= price:
        if total_inserted - price == 0:
          print("You have paid the correct amount of money and do not need any change.")
          break
        elif total_inserted > price:
            print("Your change is",calculate_change(total_inserted,price),"pence.")
            break

    if total_inserted < price:
        coin_inserted = int(input("You need to insert more coins for the payment, please insert another coin"))
        if coin_inserted == 20 or coin_inserted == 5 or coin_inserted == 10:
            total_inserted += coin_inserted
            continue

    if coin_inserted != 20 or coin_inserted != 5 or coin_inserted != 10:
        print("This machine does not accept that coin.Please try again with an accepted coin.")










    