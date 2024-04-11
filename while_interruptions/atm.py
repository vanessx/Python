cash = int(input('How much money do you want to withdraw? '))
total = cash
note = 50
totnote = 0

while True:
    if total >= note:
        total -= note
        totnote += 1
    else:
        if totnote > 0: # só printa as notas que forem usadas
            print(f'Total of {totnote} notes of {note}€')
        if note == 50:
            note = 20
        elif note == 20:
            note = 10
        elif note == 10:
            note = 1
        totnote = 0
        if total == 0:
            break