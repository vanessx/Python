x = float(input('First grade (1-10): '))
y = float(input('Second grade (1-10): '))

average = (x + y) / 2

if average < 5:
    print('\033[31mRejected!\033[m')
elif average >= 5 and average < 7:  # poderia ser 7 > average >= 5
    print('\033[33mSummer school!\033[m')
else:
    print('\033[32mApproved!\033[m')
