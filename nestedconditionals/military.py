from datetime import date

year = int(input('What year were you born? '))
current_year = date.today().year
years_old = current_year - year

if years_old < 18:
    x = 18 - years_old
    print(f'You will enlist in {x} years. It will be {current_year + x}.')
elif years_old == 18:
    print('It is time to enlist.')
else:
    x = years_old - 18
    print(f'{x} years have passed to enlist. It should have been in {current_year - x}.')
