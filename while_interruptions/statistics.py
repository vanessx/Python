total = sum = cheap = count = 0
cheap_product = ' '

while True:
    product = input('Product: ').title()
    price = float(input('Price: €'))
    count += 1
    sum += price
    if price > 1000:
        total += 1
    if count == 1 or price < cheap:
        cheap = price
        cheap_product = product
    repeat = ' '
    while repeat not in 'yn':
        repeat = input('Do you want to continue? [Y/N]: ').lower().strip()[0]
    if repeat == 'n':
        break

print(f'The total cost is {sum:.2f}€')
print(f'{total} products cost more than 1.000€')
print(f'{cheap_product} is the cheapest. It cost {cheap:.2f}€')