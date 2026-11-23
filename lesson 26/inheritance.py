class familymember:
    def __init__(self,eye_colour,height):
        self.eye_colour = eye_colour
        self.height = height
    def show_traits(self):
        pass
class kid(familymember):
    def __init__(self,sports,hair_col,eye_colour,height):
        self.sports = sports
        self.hair_col = hair_col
        super().__init__(eye_colour,height)
    def show_traits(self):
        print(f"The sport of the child is {self.sports}\nThe hair colour of the child is {self.hair_col} \nThe eye colour of the child is {self.eye_colour} \nThe height of the child is {self.height}.")
    def new_meth(self):
        print("I am a method that only belongs to the child.")

Kid = kid("football","blonde","blue","180 centimetres")
Kid.show_traits()
Kid.new_meth()



