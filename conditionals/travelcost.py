km = int(input('How far are you traveling in kilometres? '))

if km <= 200:
    cost = float(km * 0.50)
    print(f'The cost is {cost:.2f}€')
else:
    cost = float(km * 0.45)
    print(f'The cost is {cost:.2f}€')
