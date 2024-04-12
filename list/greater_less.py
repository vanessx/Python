numbers = []
greater = 0
less = 0

for number in range(1,6):
    numbers.append(int(input('Type a number: ')))

for pos, number in enumerate(numbers):
    if number == max(numbers):
        greater = pos
    if number == min(numbers):
        less = pos

print(f'The greater number is {max(numbers)} and it is in {greater + 1} place.\n'
      f'The less number is {min(numbers)} and it is in {less + 1} place.')