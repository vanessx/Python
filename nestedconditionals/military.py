from datetime import date

year = int(input('What year were you born? '))
current_year = date.today().year

if current_year - year < 18:
    x = 18 - (current_year - year)
    print(f'You will enlist in {x} years.')
elif current_year - year == 18:
    print('It is time to enlist.')
else:
    x = (current_year - year) - 18
    print(f'{x} years have passed to enlist.')
