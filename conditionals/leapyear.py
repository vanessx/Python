from datetime import date

year = int(input(
    'Which year do you want to know? Type 0 to find out about the current year. '))

if year == 0:
    year = date.today().year  # vai a data de hoje e pega o ano

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('It is a leap year.')
else:
    print('It is not a leap year.')
