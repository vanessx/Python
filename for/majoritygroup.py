from datetime import date

year = date.today().year
count = 0

for c in range(1, 7):
    birth = int(input('Year of birth: '))
    age = year - birth
    if age >= 18:
        count += 1

print(f'{count} people over the age of majority.\n{6 - count} people under the age of majority.')
