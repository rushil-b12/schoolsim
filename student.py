from datetime import date
from random import randint

class Student:
    def __init__(self, name='', gender='', dob=None, subjects=[]):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.subjects = subjects.copy()
        
    def __str__(self):
        return f'{self.name}: {self.gender}, {self.dob}, {self.subjects}'
        
