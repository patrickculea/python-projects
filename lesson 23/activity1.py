store_items = ["pencil","rubber","ruler","calculator"]
stock_counts = [10,2,3,0]
new_dictionary ={item:count for item, count in zip(store_items,stock_counts)}
print(f"The full inventory is {new_dictionary}.")
in_stock =[x for x in store_items if new_dictionary[x] > 0]
print(f"These are the items that are in stock{in_stock}")

