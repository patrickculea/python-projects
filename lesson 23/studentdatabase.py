student_keys=["name","age","sex","grades"]
def input_dicy():
    print("Please introduce values for name, age ,sex , and grades.")
    student_p={i:input("enter a value please.") for i in student_keys}
    return(student_p)

def nest_dict():
    n = int(input("How many students are there?"))
    nested_d = {k:input_dicy() for k in range(1,n+1)}
    return(nested_d)

nested_dictionary = nest_dict()
print(nested_dictionary)


while True:
    print("I wil give you some options to interrogate the database")
    print("a, to adjust the database")
    print("y to display students younger than 14")
    print("s to display the result of a specific student")
    print("m or f to display masculine or feminine entries")
    print("excellent to display students with grades higher than or equal to seven")
    print("stop to exit")
    option = input("")
    if option == "y":
        result = {k:v for k,v in nested_dictionary.items() if int(v["age"]) <= 14}
        print(result)
    elif option =="s":
        student = int(input("Which student?(integer value)"))
        result = {k:v for k,v in nested_dictionary.items() if k == student}
        print("result")
    elif option == "m" or option == "f":
        if option == "m":
            result = {k:v for k,v in nested_dictionary.items() if v["sex"] == "m"}
            print("result")
        else:
            result = {k:v for k,v in nested_dictionary.items() if v["sex"] == "f"}
            print(result)
    elif option == "excellent":
        result = {k:v for k,v in nested_dictionary.items() if v["grades"].isdigit() and int(v["grades"]) >= 7}
        print(result)
    elif option == "stop":
        import sys
        sys.exit()
    elif option == "a":
        adjust_r = int(input("Which registration do you want to adjust, 1 or, 2  or,3 ,etc?"))
        adjust_data = input("Press n to change their name, a to change their age, s to change their sex, g to change their grades.")
        if adjust_data =="n":
            a_name = input("Please introduce the new name.")
            nested_dictionary[adjust_r]["name"] = a_name
            print("The adjusted dictionary is now",nested_dictionary)
        elif adjust_data == "a":
            a_age = int(input("Please introduce the new age"))
            nested_dictionary[adjust_r]["age"] = a_age
            print("The adjusted dictionary is now",nested_dictionary)
        elif adjust_data == "s":
            a_sex = input("The new value for sex is")
            nested_dictionary[adjust_r]["sex"] = a_sex
            print("The adjusted dictionary is now",nested_dictionary)
        elif adjust_data == "g":
            a_grades = int(input("What is the new grades?"))
            nested_dictionary[adjust_r]["grades"] = a_grades
            print("The adjusted dictionary is now",nested_dictionary)
    else:
        print("Unacceptable input, please try again.")
            
            


