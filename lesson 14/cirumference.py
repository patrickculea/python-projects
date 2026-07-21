def circumference(radiusd,rd):
    if rd == "radius":
        print("The circumference of your circle is:", radiusd * 2 * 3.14)
    elif rd == "diameter":
        print("The cirumference of your circle is:",radiusd * 3.14)
    else:
        print("error")

def area(radiusd,rd):
    if rd == "radius":
        print("the area of your circle is:",radiusd * radiusd * 3.14)
    elif rd == "diameter":
        print("The area of your circle is:",radiusd / 2 * radiusd / 2 * 3.14)
    else:
        print("error")

choice = input("would you like me to tell you the area or the circumference of your circle?")
rd = input("would you like to tell me the radius or the diameter of your circle?")
radiusd = int(input("Please tell me the length of your choice"))

if choice == "area":
    area(radiusd,rd)
elif choice == "circumference":
    circumference(radiusd,rd)




    
    



    

    


