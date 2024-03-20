km = float(input('How far are you traveling in kilometres? '))

if km <= 200:
    cost = km * 0.50
else:
    cost = km * 0.45

print(f'The cost is \033[31m{cost:.2f}€\033[m') # a cor de texto em vermelho
