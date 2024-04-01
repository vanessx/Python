number = int(input('Type a number: '))
count = number
f = 1

print(f'Calculating {number}! = ', end = '')

while count > 0:
    print(count, end=' ')
    print('x' if count > 1 else '=', end=' ')
    f *= count
    count -= 1

print(f)