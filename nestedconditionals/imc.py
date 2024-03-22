height = float(input('Height: '))
weight = float(input('Weight: '))

imc = weight / (height * height)

if imc <= 18.5:
    print(f'Underweight! Your imc is {imc:.1f}')
elif imc <= 25:
    print(f'Ideal weight! Your imc is {imc:.1f}')
elif imc <= 30:
    print(f'Overweight! Your imc is {imc:.1f}')
elif imc <= 40:
    print(f'Obesity! Your imc is {imc:.1f}')
else:
    print(f'Morbid obesity! Your imc is {imc:.1f}')
