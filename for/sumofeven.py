sum = 0

for c in range(1, 7):
    num = int(input('Number: '))
    if num % 2 == 0:
        sum += num

print(f'The sum of the even numbers is \033[31m{sum}\033[m.')
