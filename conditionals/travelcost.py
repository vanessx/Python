km = float(input('How far are you traveling in kilometres? '))

if km <= 200:
    cost = km * 0.50
else:
    cost = km * 0.45

print(f'The cost is {cost:.2f}€')
