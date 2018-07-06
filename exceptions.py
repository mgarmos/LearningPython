name = input("Input your name: ")
age = input('Input your age: ')

try:
    print('You where born in {}. '.format(2018 - int(age)))
except ValueError:
    print(age + ' is not a number')

