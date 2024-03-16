days = int(input('How many days? '))
km = float(input('How many kilometres? '))
per_day = 30 * days
per_km = km * 0.15
total = per_day + per_km
print(f'The total cost is {total}')
