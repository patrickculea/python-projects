med_cause =input("Do you have a medical cause? {Y/N}").strip().upper()
if med_cause == "Y":
    print("You can take the test")
else:
    att = int(input("what is your attendance?"))
    if att >= 75:
        print("you can take the test.")
    else:
        print("you are not allowed to take the test.")