print("ASCII value checker")
char = input("give me a charachter and i will tell you its ASCII value.")
if type(char) is str and len(char) == 1:
    ASCII_val = ord(char)


    print(f"charachter: {char}")

    print(f"ASCII Value: {ASCII_val}")

    print("\n=Charachter Type:", end="")

    if ASCII_val >= 65 and ASCII_val <= 90:
        print("its an uppercase letter")

    elif ASCII_val >= 97 and ASCII_val <= 122:
        print("its a lowercase letter")

    elif ASCII_val >=48 and ASCII_val <= 57 :
        print("its a digit")

    elif ASCII_val ==32:
        print("its a space")
    else:
        print("it is a special charachter")
else:
    print("I told you to print only 1 charachter")