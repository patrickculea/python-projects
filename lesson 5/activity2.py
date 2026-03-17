buying =int(input("what is the buying price?"))
selling =int(input("what is the selling price?"))
if selling > buying :
    profit =selling - buying
    print(f"the profit is {profit}")
else:
    loss =buying - selling
    print(f"the loss is {loss}")