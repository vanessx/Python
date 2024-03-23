sum = 0
count = 0

for c in range(1, 7):
    num = int(input(f'Number {c}: '))
    if num % 2 == 0:
        sum += num
        count += 1

print(f'The sum of {count} even numbers is \033[31m{sum}\033[m.')
