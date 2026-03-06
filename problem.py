s1_name = "Faraz"
s1_id = 23
s1_attendance = 95
s1_marks = 78

s2_name = "Qasim"
s2_id = 56
s2_attendance = 56
s2_marks = 66

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >=70:
        return "B"
    elif marks >=50:
        return "C"
    else:
        return "Fail"
    
def update_marks(old_marks,new_marks):
    return new_marks
print("student1  name :", s1_name)
print("student1 id :", s1_id)
print("student1 attendance :", s1_attendance)
print("======================================")
print("student2 name  :", s2_name)
print("student2 id :", s2_id)
print("student2 attendance :", s2_attendance)
print("calculate grade : ", calculate_grade(89))
# print("update marks :", update_marks(34,78))
s2_mark = update_marks(s2_marks,87)
print("After update")
print("name :", s2_name)
print("marks :",s2_mark)
print("attendance :", s2_attendance)
print("id :", s2_id)
