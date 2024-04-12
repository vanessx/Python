numbers = tuple(int(input('Type a number: ')) for c in range(1,5))

print('The numbers you typed are: ')
for number in numbers:
    print(number)

print(f'The number 9 appeared {numbers.count(9)} times.')

if 3 in numbers:
    print(f'The number 3 is {numbers.index(3) + 1} place.')

for number in numbers:
    if number % 2 == 0:
        print(f'The number {number} is even.')