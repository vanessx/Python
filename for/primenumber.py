num = int(input('Number: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        total += 1 # vai acumular quantas vezes o número é divisivel

if total == 2: # só é primo se for divisivel por 1 e por ele mesmo
    print(f'The number {num} is a prime number.')
else:
    print(f'The number {num} is not a prime number.')
