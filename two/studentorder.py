from random import sample

first_name = input('First name: ')
second_name = input('Second name: ')
third_name = input('Third name: ')
fourth_name = input('Fourth name: ')
fifth_name = input('Fifth name: ')

list = [first_name, second_name, third_name, fourth_name, fifth_name]

print(sample(list, len(list)))
