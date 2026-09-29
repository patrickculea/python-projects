basket_1 ={"orange","mango","pinneaple","orange","apple","grapes"}
print(basket_1)
basket_2 ={"pinneaple","pinneaple","pinneaple","orange","mango","Passion fruit"}
print(basket_2)

basket_1.add("coconut")
print(basket_1)

print("The common items betweeen basket 1 and basket 2 are :",basket_1.intersection(basket_2))

import array as ar

fruit_count =ar.array("i",[5,1,6,3,2,5,3,5,6,9])
print(fruit_count)
fruit_count.insert(1,12)
print(fruit_count)
fruit_count.append(13)
print(fruit_count)
print(fruit_count.count(5))
fruit_count.reverse()
print(fruit_count)




