print("Mirrorred right angle triangle.")
row = int(input("How many rows should it have?"))
for i in range(row):
    for j in range(1,row + 1):
        if j < row - i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
    

