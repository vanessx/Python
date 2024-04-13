values = []

while True:
    value = int(input('Type a number: '))
    if value not in values:
        values.append(value)
        print('Added value!')
    else:
        print('This value is already on the list.')
    repeat = input('Do you want to continue? [Y/N]: ').lower()
    if repeat == 'n':
        break

values.sort()
print('The values on the list are:')
for value in values:
    print(value, end=' ')