speed = int(input('How fast is the car going? '))

if speed > 80:
    print(f'{speed}Km/h? Too fast! Fined.')
    fine = float((speed - 80) * 7)
    print(f'The amount of the fine is {fine:.2f}€')
else:
    print('Doing well!')
