matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
total = sumcol = 0

for l in range(0, 3):
    for c in range (0, 3):
        matrix[l][c] = int(input('Type a number: '))
        if matrix[l][c] % 2 == 0:
            total += matrix[l][c]

for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matrix[l][c]}]', end = '')
    print()

for l in range(0, 3):
    sumcol += matrix[l][2] 

print(f'The sum of even numbers is: {total}\n'
      f'The sum of the numbers in the third column is: {sumcol}\n'
      f'The greater number in the second line is: {max(matrix[1])}')