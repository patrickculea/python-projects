class IOString:
    def __init__(self,str1):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Please give me a string.")
        print("Thank you.")
    def print_string(self):
        self.str1 = self.str1.upper()
        print(f"The string you gave me in upppercase is {self.str1}")

str1 = IOString("hi")
str1.get_string()
str1.print_string()
        