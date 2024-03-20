print('-=-' * 6)
print('Triangle Analysis')
print('-=-' * 6)

a = int(input('First line: '))
b = int(input('Second line: '))
c = int(input('Third line: '))

if a < b + c and b < a + c and c < a + b:  # um é sempre menor que a soma dos outros dois
    print('You can form a triangle')
else:
    print('You cannot form a triangle')
