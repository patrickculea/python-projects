models =["Toyota prius","lamborghini aventador","Ferrari enzo"]
fuel_consumption =[3.5,8.0,24]
cylinders= [4,5,6]
prices = [3000,500000,1000000]
fuel_type = ["hybrid","deisel","petrol"]
deisel_discount = lambda price : price * 0.9
hybrid_discount = lambda price : price * 0.85
petrol_discount = lambda price : price * 0.95
car_database = zip(models,fuel_consumption,cylinders,fuel_type,prices)
for models,fuel_consumption,cylinders,fuel_type,prices in car_database:
    print(f"The model is {models}.")
    print(f"Its fuel consumption in litres per 100km is {fuel_consumption}.")
    print(f"It has {cylinders} cylinders in its engine.")
    print(f"The fuel type is {fuel_type}.")
    print(f"The price is {prices} GBP.")
    if fuel_type =="hybrid":
        print("After the hybrid discount,the price is",hybrid_discount(prices),"GBP")
    if fuel_type == "petrol":
        print("After the petrol discount the final price of the car is",petrol_discount(prices),"GBP")
    if fuel_type == "deisel":
        print("After the deisel discount the final price of the car is",deisel_discount(prices),"GBP")

