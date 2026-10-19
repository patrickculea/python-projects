books=["animal farm","1984","harry potter","skandar","eragon"]
copies = [0,2,0,4,6]
library = {k:int(v) for k,v in zip(books, copies)}
print("The books that are in stock are:")
in_stock = {k:v for k,v in library.items() if v > 0}
print(in_stock)
choice = input(f"The books this library has, are{books}, which one would you like to borrow")
if library[choice] > 0:
    print("That book is in stock.")
    library[choice] - 1
else:
    print("That book is not in stock.")
    import sys
    sys.exit()

late_fees = [5, 8, 4, 6 ,7]
extra_fee = int(input("Enter the  extra library fee to add to every book"))

updated_fees=list(map(lambda a: a + extra_fee,(late_fees)))

print(f"There are {library[choice]} copies of {choice} left.")
print("Library summary")
print("The books we currently have in stock are:", in_stock)
print("The late fees are", updated_fees)
print("============================================")









