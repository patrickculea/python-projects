print("Give me five snack items ,some of them should repeat but there should be 5 in total. I will make them a set. I will do this twice")


snack_set = set()
def set_maker():
    n = int(input("How many snacks should there be in this set"))
    for i in range (n) :
    
        a = input("Next snack =")
        snack_set.add(a)

    return snack_set

snackset_1 =set_maker()

print("again.")
snackset_2 =set_maker()

choice = input("Would you like to add banana to snackset_1?")
if choice == "yes":
    snackset_1.add("banana")
    print(f"The updated snackset_1 is {snackset_1}.")
else:
    print(f"Ok, snackset_1 remains as {snackset_1}.")

x = snackset_1.intersection(snackset_2)
print(f"The common snacks that re both in snackset_1 and in snackset_2 are {x}.")

import array as arr

array_amount = int(input("How many integer values do you want to add in snack_counts?"))

snack_counts=arr.array("i",[])

for i in range(array_amount):
    add =int(input("The next integer value you want to add to snack_counts array is:"))
    snack_counts.append(add)

print(f"the normal snack_counts array is {snack_counts}.")
snack_counts.reverse()
print("The reversed snack_counts array is",snack_counts)

count_of_5 =snack_counts.count(5)
print(f"The number of times the number 5 appears in the snack_counts array is{count_of_5}")

print("=====SCHOOL SNACK COUNTER=====")
print("snackset_1 =",snackset_1)
print("snackset_2 =",snackset_2)
print("shared snacks =",x)
print("Snack counts:",snack_counts)
print("============================================================================================================================================================================")




    
    







    