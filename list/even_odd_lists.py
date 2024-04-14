numbers = [[], []]

for c in range(1,8):
    num = int(input('Type a number: '))
    if num % 2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)    

print(f'The list of even numbers: {sorted(numbers[0])}\n'
      f'The list of odd numbers: {sorted(numbers[1])}')
