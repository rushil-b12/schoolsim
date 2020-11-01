from subjgen import *

class Student:
    def __init__(self, name, gender, dob, subjects = []):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.subjects = subjects if check_subjects(subjects) else choose_subjects()
        
    def __str__(self):
        return f'{self.name}: {self.gender}, {self.dob}, {self.subjects}'
        
    
a = Student('rushil', 'M', '12MAY06', [])
print(a)