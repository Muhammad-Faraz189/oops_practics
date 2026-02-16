# class creation:
# class car:
#     # attributes:
#     color = "Black"
#     price = 100000
#     number_plate = 5582
#     #object creation:
# obj_1 = car()
# obj_2 = car()
# obj_3 = car()
# print(obj_1.color)  
# print(obj_1.price)

# ________________________________________________#

class Teacher(): #class
    def __init__(self,Teacher_name:str,Teacher_id:int):   #constructor
        self.Teacher_name:str = Teacher_name              #attributes
        self.Teacher_id:int = Teacher_id                  #self.atttributes_name = value
    def speak(self):                                      #method / All methods must have self as the first parameter.
        print(f"{self.Teacher_name} is speaking about atheics in the classroom.")
    def teaching(self):                                   #method
        print(f"{self.Teacher_name} is teaching us AI and data science. Sir id is {self.Teacher_id}.")
obj_1 =Teacher("Sir Naveed Sarwar", 1122)                  #objects
obj_2=Teacher("Sir Qassim", 5582)
obj_1.speak()
obj_2.teaching()


