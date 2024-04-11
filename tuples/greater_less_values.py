from random import randint

numbers = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'This is the list: {numbers}')

less = 0
greater = 0
for number in numbers:
    if number == numbers[0]:
        less = number
        greater = number
    elif number > greater:
        greater = number
    elif number < less:
        less = number

print(f'{greater} is the greater and {less} is the less one.')

# solução mais simples
print(f'The greater is {max(numbers)} and the less is {min(numbers)}.')