matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range (0, 3):
        matrix[l][c] = int(input('Type a number: '))

for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matrix[l][c]}]', end = '')
    print()
