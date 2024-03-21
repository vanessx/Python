print('-=-' * 6)
print('Triangle Analysis')
print('-=-' * 6)

a = int(input('First line: '))
b = int(input('Second line: '))
c = int(input('Third line: '))

if a < b + c and b < a + c and c < a + b:
    print('You can form a triangle.')
    if a == b and b == c:
        print('Is an equilateral triangle.')
    elif a == b or b == c or a == c:
        print('Is an isosceles triangle.')
    else:
        print('Is a scalene triangle.')
else:
    print('You can not form a triangle.')
