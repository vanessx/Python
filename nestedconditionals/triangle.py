print('-=-' * 6)
print('Triangle Analysis')
print('-=-' * 6)

colors = {'close': '\033[m',
        'red': '\033[31m',
        'green': '\033[32m'}

a = int(input('First line: '))
b = int(input('Second line: '))
c = int(input('Third line: '))

if a < b + c and b < a + c and c < a + b:
    print(colors['green'],'You can form a triangle.', colors['close'])
    if a == b and b == c:
        print('Is an equilateral triangle.')
    elif a == b or b == c or a == c:
        print('Is an isosceles triangle.')
    else:
        print('Is a scalene triangle.')
else:
    print(colors['red'],'You can not form a triangle.', colors['close'])
