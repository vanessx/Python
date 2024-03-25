age_sum = 0
older = 0
older_person = ''
total_women = 0

for c in range(1, 5):
    print(f'----- PERSON NUMBER {c} -----')
    name = input('Name: ').strip()
    age = int(input('Age: '))
    sex = input('Gender? [M/F] ').lower().strip()
    # soma todos os 4 inputs de idade em um acumulador (age_sum)
    age_sum += age
    if c == 1 and sex == 'm':  # podia ser sex in 'Mm' caso o user digitasse m ou M, mas como usei lower() nao usei esta maneira
        older = age
        older_person = name
    if age > older and sex == 'm':
        older = age
        older_person = name
    if age > 18 and sex == 'f':
        total_women += 1

average_age = age_sum / 4

print(f'The average age is {average_age}.')
print(f'{older_person} is the older men.'.capitalize())
print(f'The total number of women over 18  is {total_women}.')
