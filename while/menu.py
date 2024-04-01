n1 = int(input('Number: '))
n2 = int(input('Number: '))
# declarar como zero para que possamos usar
option = 0

while option != 5:
    option = int(input('[1] to sum\n[2] to multiply\n[3] greater\n[4] new numbers\n[5] to exit '))
    if option == 1:
        print(f'The sum is {n1 + n2}\n')
    elif option == 2:
        print(f'The multiplication is {n1 * n2}\n')
    elif option == 3:
        if n1 > n2:
            print(f'{n1} is greater than {n2}\n')
        elif n1 < n2:
            print(f'{n2} is greater than {n1}\n')
        else:
            print(f'{n1} is equal to {n2}\n')
    elif option == 4:
        n1 = int(input('Number: '))
        n2 = int(input('Number: '))
    elif option == 5:
        print('Exiting...')
    else:
        print('Try again.')

print('Exited.')
