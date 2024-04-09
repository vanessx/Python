first = int(input('First term: '))
ratio = int(input('Ratio: '))
term = first
count = 1
total = 0
more = 10

while more != 0:
    total += more
    while count <= total:
        print(f'{term}', end=' ')
        term += ratio
        count += 1
    more = int(input('How many more terms do you want to show? '))