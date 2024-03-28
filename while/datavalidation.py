# o [0] só vai pegar a primeira letra
gender = input('What is your gender? [F/M] ').lower().strip()[0]

# podia também ser while gender not in 'fm':
while gender != 'f' and gender != 'm':
    gender = input('Please, type a valid gender. [F/M]')

if gender == 'f':
    print('Registered female.')
else:
    print('Registered male.')
