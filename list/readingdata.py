numbers = []

while True:
    num = int(input('Type a number: '))
    numbers.append(num)
    repeat = input('Do you want to continue? [Y/N]: ').lower()
    if repeat == 'n':
        break

print(f'The total of numbers entered is {len(numbers)}.')
print(f'The list in descending order is {sorted(numbers, reverse=True)}')

if 5 not in numbers:
    print('The number 5 is not on the list.')
else:
    print('The number 5 is on the list.')