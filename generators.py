from random import choice, randint
from datetime import date
from student import Student
from classs import Class

subjects = {'sciences': ['biology', 'physics', 'chemistry'], 'humanities': ['geography', 'history', 'economics', 'computerscience', 'psychology', 
'politics', 'business', 'environmental'], 'arts': ['music', 'art', 'film', 'drama', 'designtechnology'], 'languages': ['chinese', 'spanish', 'french', 'german']}

def choose_subjects():
    chosen = ['english', 'maths']
    for k, v in subjects.items():
        if k == 'sciences' or k == 'humanities':
            sub1 = choice(v)
            chosen.append(sub1)
            sub2 = choice(v)
            while sub2 == sub1:
                sub2 = choice(v)
            chosen.append(sub2)
        else:
            chosen.append(choice(v))
    return chosen

def check_subjects(chosen):
    if len(chosen) == 8:
        if chosen[0] == 'english':
            if chosen[1] == 'maths':
                if chosen[2] in subjects['sciences'] and chosen[3] in subjects['sciences']:
                    if chosen[4] in subjects['humanities'] and chosen[5] in subjects['humanities']:
                        if chosen[6] in subjects['arts']:
                            if chosen[7] in subjects['languages']:
                                return True
    return False

def generate_date():
    m = randint(1,12)
    if m in [1, 3, 5, 7, 8, 10, 12]:
        d = randint(1, 31)
    elif m in [4, 6, 9, 11]:
        d = randint(1, 30)
    if m > 8:
        y = randint(2002, 2005)
    else:
        y = randint(2003, 2006)
    if y % 4 == 0 and m == 2:
        d = randint(1, 29)
    elif y % 4 != 0 and m == 2:
        d = randint(1, 28)
    dob = date(y, m, d)
    return dob

def checkdate(date):
    if date.month in [1, 3, 5, 7, 8, 10, 12]:
        if 0 < date.day < 32:
            return True
    elif date.month in [4, 6, 9, 11]:
        if 0 < date.day < 31:
            return True
    elif date.year % 4 == 0 and date.month == 2:
        if 0 < date.day < 30:
            return True
    elif date.year % 4 != 0 and date.month == 2:
        if 0 < date.day < 29:
            return True
    return False

def generate_name():
    with open('../poodles/male.txt', 'r', encoding="utf8") as mfile:
        content = mfile.readlines()
        m = choice(content)[:-1]

    with open('../poodles/female.txt', 'r', encoding="utf8") as ffile:
        content = ffile.readlines()
        f = choice(content)[:-1]
    
    return m, f

def generate_student():
    x = randint(0, 1)
    name = generate_name()[x]
    gender = 'M' if x == 0 else 'F'
    dob = generate_date()
    subjects = choose_subjects()
    
    return Student(name, gender, dob, subjects)
    
def generate_class(number_of_students):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    letter = alphabet[randint(0, len(alphabet))]
    alphabet.remove(letter)
    return Class(letter, [generate_student() for i in range(number_of_students)])

if __name__ == '__main__':
    print(generate_student())
        