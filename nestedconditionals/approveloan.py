house = float(input('House price: '))
salary = float(input('Your salary: '))
years = int(input('How many years will you pay it off: '))

loan = house / (years * 12)
amount_available = salary * 0.30

if loan >= amount_available:
    print('\033[31mNot approved!\033[m')
else:
    print(f'\033[32mApproved!\033[m\nThe amount to be paid will be {loan:.2f}€')
