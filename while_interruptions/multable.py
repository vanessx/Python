while True:
    number = int(input('The multiplication table of: '))
    if number < 0:
        break
    for c in range(1, 11):
        print(f'{number} x {c} = {number * c}')
