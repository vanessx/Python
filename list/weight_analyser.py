people = []
data = []
more = less = 0

while True:
    name = input('Name: ')
    weight = float(input('Weight: '))
    data.append(name)
    data.append(weight)
    if len(people) == 0:
        more = less = data[1]
    else:
        if data[1] > more:
            more = data[1]
        if data[1] < less:
            less = data[1]

    people.append(data[:])
    data.clear()

    repeat = input('Do you want to continue? [Y/N]: ').lower()
    if 'n' in repeat:
        break

print(f'{len(people)} people were registered.')
print(f'The highest weight is {more}kg. The weight of ', end='')

for person in people:
    if person[1] == more:
        print(f'[{person[0].title()}] ', end='')

print(f'\nThe lowest weight is {less}kg. The weight of ', end='')

for person in people:
    if person[1] == less:
        print(f'[{person[0].title()}] ', end='')
