digit = int(input('Enter a number between 0 and 9999: '))
u = digit // 1 % 10
d = digit // 10 % 10
h = digit // 100 % 10
t = digit // 1000 % 10
print(f'Unit: {u}\nDozen: {d}\nHundred: {h}\nThousand: {t}')
