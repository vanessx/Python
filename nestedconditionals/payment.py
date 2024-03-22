colors = {'close': '\033[m',
          'red': '\033[31m',
          'cyan': '\033[36m',
          'green': '\033[32m',
          'purple': '\033[35m'}

background = {'red': '\033[41m',
              'cyan': '\033[46m',
              'green': '\033[42m',
              'purple': '\033[45m'}

product = float(input('Product price: '))
payment = int(input(f'''{background['red']}Cash payment{colors['close']} {colors['red']}[press 1]{colors['close']}
{background['cyan']}Payment by card{colors['close']} {colors['cyan']}[press 2]{colors['close']}
{background['green']}Double payment by card{colors['close']} {colors['green']}[press 3]{colors['close']}
{background['purple']}Triple payment or more by card{colors['close']} {colors['purple']}[press 4]{colors['close']}'''))

if payment == 1:
    total = product - (product * 0.10)
elif payment == 2:
    total = product - (product * 0.05)
elif payment == 3:
    total = product
elif payment == 4:
    total = product + (product * 0.20)

print(f'\033[7mThe total to pay is {total:.2f}€\033[m')