count_age = count_men = count_women_less20 = 0

while True:
    age = int(input('Age: '))
    gender = ' '
    while gender not in 'fm':
        gender = input('Gender [F/M]: ').lower().strip()[0]
    if age >= 18:
        count_age += 1
    if gender == 'm':
        count_men += 1
    if age < 20 and gender == 'f':
        count_women_less20 += 1
    repeat = ' '
    while repeat not in 'yn':
        repeat = input('Do you want to continue? [Y/N]: ').lower().strip()
    if repeat == 'n':
        break

print(f'{count_age} people are 18 or more years old.')
print(f'\n{count_men} people are men.')
print(f'\n{count_women_less20} people are women under 20 years old.')
