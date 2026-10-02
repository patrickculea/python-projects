print("Give me five snack items ,some of them should repeat but there should be 5 in total. I will make them a set")
n = int(input("How many valus should each of the sets have?"))

snack_set = set()
def set_maker(n,0):
    for i in range (n) :
    
        a = input("Next value =")
        snack_set.add(a)

set_maker(n,0)

snack_set1 = snack_set

print("again.")
set_maker(n,snack_set)
snack_set2 = snack_set




    