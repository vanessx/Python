sum = 0 # acumulador
count = 0 # contador

for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        sum += c

print(f'The sum of all \033[33m{count}\033[m values is \033[31m{sum}\033[m.')
