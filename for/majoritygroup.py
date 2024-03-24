from datetime import date

year = date.today().year
count_over = 0
count_under = 0

for c in range(1, 7):
    birth = int(input('Year of birth: '))
    age = year - birth
    if age >= 18:
        count_over += 1
    else:
        count_under += 1

print(f'{count_over} people over the age of majority.\n{count_under} people under the age of majority.')
