class Student:
    def __init__(self, name, gender, dob, subjects = []):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.subjects = subjects if len(subjects) == 4 else 
        
    def __str__(self):
        return f'{self.name}: {self.gender}, {self.dob}, {self.subjects}'
        
    
a = Student('rushil', 'M', '12MAY06', ['geo', 'cs', 'french', 'drama'])
print(a)