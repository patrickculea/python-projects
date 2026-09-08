
"""Step 1: Create an empty list called empty_list and print a blank line.

Step 2: Create a list called numbers holding five integers and print it.

Step 3: Use the * operator to repeat [1, 2, 3] three times and store it in triples.

Step 4: Print the triples list.

Step 5: Create a list called aList holding five numbers.

Step 6: Reverse aList using slicing with [::-1] and store it back into aList.

Step 7: Print the reversed aList"""

empty_list =[]
print(empty_list)
numbers = [1,2,3,4,5]
print("The list of integers is:",numbers)
triples = [1,2,3] * 3
print("The triples list is:",triples)
aList1 =[11,12,13,14,15]
aList = aList1[::-1]
print("The normal list is",aList1)
print("The reversed list is",aList)

aList2 =len(aList1)
print(f"The length of Alist1 is:{aList2}")
print("The last item in the numbers list is:",numbers[-1])
print("The first item in the numbers list is:",numbers[0])


