students = {"ava":30,"john":50,"dave":90,"elijah":70,"betty":45}
avg = 0
names =[]
print(f"The students and their scores are:{students}.")
grades=[]
for k,v in students.items():
    avg += v / 5
    x = students.get(k)
    grades.append(x)
    names.append(k)
print("The class average is",avg)
print("The highest grade in the class was",max(grades))
print("The lowest score was",min(grades))
choice = input(f"Which student,{names} ,would you like to know the grades of?")
print(f"The grade of {choice} is",students.get(choice))





