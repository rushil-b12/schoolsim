from classs import Class
from student import Student
from generators import *

def database():
    classes = []
    classes.append(generate_class(6))
    classes.append(generate_class(4))
    return classes


def run():
    classes = database()
    [print(c) for c in classes]
    return classes
