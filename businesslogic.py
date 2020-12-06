from database import run
from generators import *

classes = run()

def get_student_from_class(classname, student):
    for c in classes:
        if c.classname == classname:
            for s in c.students:
                if s.name == student:
                    return s

def get_class(classname, pw):
    for c in classes:
        if c.classname == classname:
            if pw == 'confusing':
                return c