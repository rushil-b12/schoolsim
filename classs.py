from student import Student
from datetime import date
from random import randint
# from generators import *

class Class:
    def __init__(self, classname='', students = []):
        self.students = students.copy()
        self.classname = classname 

    def __str__(self):
        return f'Class {self.classname}: {[s.name for s in self.students]}'

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, removing):
        for s in self.students:
            if s.name == removing:
                self.students.remove(s)

# if __name__ == '__main__':
    # c = Class('A', [generate_student(), generate_student()])
    # print(c)
    # for i in range(3):
    #     c.add_student(generate_student())
    #     print(c)
    # d = Class('B', [Student('Rushil', 'M'), generate_student()])
    # print(d)