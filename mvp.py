from businesslogic import *


x = input('Are you a teacher or a student? Enter T or S ')
if x.lower() == 't':
    y = input('''What would you like to do? 
    Enter:
    1 to display your class, 
    2 to display a student,
    3 to add a student to a class
    4 to remove a student from a class. \n ''')
    z = input('What is the classname of your class? ')
    pw = input('Please enter the password (\'confusing\') ')
    if y == '1':
        print(get_class(z, pw))
    elif y == '2':
        a = input('What is the name of the student?')
        print(get_student_from_class(z, a))
    elif y == '3':
        pass
    elif y == '4':
        pass
elif x.lower() == 's':
    y = input('What class are you in? ')
    z = input('What is your name? ')
    print(get_student_from_class(y, z))
else:
    print('That is not an option.')