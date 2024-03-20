salary = float(input('How much is your salary? €'))

if salary > 1250:
    new_salary = salary + (salary * 0.10)
else:
    new_salary = salary + (salary * 0.15)

print(f'Your new salary is {new_salary:.2f}€')