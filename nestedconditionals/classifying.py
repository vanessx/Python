from datetime import date

year = int(input('What year were you born? '))
current_year = date.today().year

years_old = current_year - year

if years_old <= 9:
    print('CHILD')
elif years_old <= 14:
    print('INFANTILE')
elif years_old <= 19:
    print('JUNIOR')
elif years_old <= 20:
    print('SENIOR')
else:
    print('MASTER')
