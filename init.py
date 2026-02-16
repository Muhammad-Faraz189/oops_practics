# initialized the class:
class school:
    # Under class we have fixed attributes.
    school_name = "GOVT.united muslim high school."
    # init constructor:
    def __init__(self, name,age):
        # Under __init__ we have instance attributes.
        self.name = name
        self.age = age      
obj_1 = school("Faraz",25)
print(obj_1.name)
print(obj_1.age)  
print(obj_1.school_name)
# or
print(school.school_name)      
