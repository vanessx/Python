n = int(input('Number: '))
f = 1

for num in range(n, 0, -1):
    print(num, end=' ')
    print('x' if num > 1 else '=', end=' ')
    f *= n
    n -= 1

print(f)
