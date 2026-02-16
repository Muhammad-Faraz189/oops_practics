class Employ():
    def __init__(self) -> None:
        self.name: str = None
        self.age: int = None
        self.department: str = None
        self.education: str = None


class Designer(Employ):
    def __init__(self, title: str) -> None:
        super().__init__()
        self.title: str = title


class Developer(Employ):
    def __init__(self, title: str) -> None:
        super().__init__()
        self.title: str = title
        self.programming_skill: list = ["Python"]


designer1: Designer = Designer("Animation Artist")
Developer1: Developer = Developer("GenAI engineer")


print(designer1.title)
print(Developer1.programming_skill)



#============================================================#



class parents():
    def __init__(self)->None:
        self.eye_color = "Brown"
        self.hair_color = "Black"
    def speak(self,word):
        print(f"Faraz is speaking {word}.")
    def watching(self,see):
        print(f"you are looking {see}.")
class child(parents):
    def height(self,number:float):
        print(f"child height is {number}")        
obj:parents = parents()
print(obj.eye_color) 
print(obj.hair_color)
obj.speak("truth") 
obj.watching("forward")
print('=======child_object==============')
obj_2:child =child()
obj_2.height(5.8)
print(obj_2.eye_color)
print(obj_2.hair_color)
obj_2.speak("fastly")

#=============================================================================#

