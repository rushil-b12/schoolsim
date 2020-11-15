from random import randint
from datetime import date

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

