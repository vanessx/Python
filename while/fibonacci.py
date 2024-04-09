n = int(input('What many terms do you want? '))
first = 0
second = 1
count = 3
print(f'{first} - {second}', end=' ')

while count <= n:
    third = first + second
    print(f'- {third}', end=' ')
    first = second
    second = third
    count += 1