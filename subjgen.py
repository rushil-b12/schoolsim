from random import choice
subjects = {'humanities': ['geography', 'history', 'economics', 'computerscience', 'psychology', 'politics', 'business',
 'environmental'], 'arts': ['music', 'art', 'film', 'drama', 'dt'], 'language': ['chinese', 'spanish', 'french', 'german']}

def choose_subjects():
    chosen = []
    for k, v in subjects.items():
        if k == 'humanities':
            hums1 = choice(v)
            chosen.append(hums1)
            hums2 = choice(v)
            while hums2 == hums1:
                hums2 = choice(v)
            chosen.append(hums2)
        else:
            chosen.append(choice(v))
    return chosen
print(choose_subjects())
        