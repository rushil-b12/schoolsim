from random import choice
subjects = {'sciences': ['biology', 'physics', 'chemistry'], 'humanities': ['geography', 'history', 'economics', 'computerscience', 'psychology', 
'politics', 'business', 'environmental'], 'arts': ['music', 'art', 'film', 'drama', 'dt'], 'languages': ['chinese', 'spanish', 'french', 'german']}

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

if __name__ == '__main__':
    print(choose_subjects())
        