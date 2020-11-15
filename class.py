from student import Student

class Class:
    def __init__(self, classname = '', students = []):
        if len(students) > 4:
            self.students = students
        else:
            for i in range(5):
                self.students.append(Student)
    
    def __str__(self):
        return f'Class {classname}: {students}'

c = Class([])
print(c)