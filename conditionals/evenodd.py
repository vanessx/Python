number = int(input('Write a number: '))

if number % 2 == 0:
    print('\033[32;43mEven!\033[m')
else:
    print('\033[31;40mOdd!\033[m')