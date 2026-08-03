print("==== VENDING MACHINE ====")
runagain = True
while (runagain == True):
    item =input("Would you like doritos or twix?")
    if item == "doritos":
         print("doritos cost 25p.")
         break
    elif item == "twix":
        price = 20
        print("twix cost 20p")
        break
    elif item != ("twix" or "doritos"):
        print("I do not sell that. Please purchase a valid item")


print("This machine only accepts 5p coins, 10p coins, and 20p coins.")
paid = False
payment = 0
change = 0

while paid == False:
    if payment > price:
        print("You have payed me too much money.")
        change = payment - price
        print(f"Your change is {change}pence.")
        paid = True
        break


    if payment == price:
        print("You have completed the transaction. Recieve your snack.")
        paid = True
        break

    coin = int(input("Please insert an accepted coin for the payment."))
    if coin ==5 or 10 or 20:
        payment += coin
        continue

        





