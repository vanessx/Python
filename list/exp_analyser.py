expression = []

exp = input('Type an expression: ')

for c in exp:
    if c == '(':
        expression.append('(')
    elif c == ')':
        if len(expression) > 0:
            expression.pop()
        else:
            expression.append(')')
            break

if len(expression) == 0:
    print('Validated expression.')
else:
    print('Expression not validated.')