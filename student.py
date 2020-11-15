from subjgen import *
from datetime import date
from random import randint
from dategen import *

class Student:
    def __init__(self, name='', gender='', dob = date(), subjects=[]):
        self.name = name
        self.gender = gender
        self.dob = dob if checkdate(dob) else generate_date()
        self.subjects = subjects if check_subjects(subjects) else choose_subjects()
        
    def __str__(self):
        return f'{self.name}: {self.gender}, {self.dob}, {self.subjects}'
        
    
a = Student('rushil', 'M', date(2006, 5, 12))
print(a)