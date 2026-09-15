empty_list= []
marks_list =[1,2,3,4,5]
print(marks_list)
sample_list =[10,20,30,] *2
print("The length of marks_list is:",len(marks_list))
print("The first value in marks_list is :",marks_list[0])
print("The last value in marks_list is :",marks_list[-1])
print("The first 3 marks of marks_list are:", marks_list[0:3])
print("The marks list reversed is :",marks_list[::-1])

def iterate():
    val_one = marks_list[0]
    val_two = marks_list[-1]
    if val_one == val_two:
        print("The first and last values of marks_list are the same.")
    else:
        print("The first and last values of marks_list are diefferent.")

iterate()

markslist_avg = marks_list[0] + marks_list[1] + marks_list[2]+marks_list[3] + marks_list[4]
print("The avergae of the values in marks_list is:",markslist_avg / 5)


