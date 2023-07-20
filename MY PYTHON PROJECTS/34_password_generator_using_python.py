import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_'

password_length = int(input('Enter the length of required password : '))
password_count = int(input('Enter the number of required passwords : '))

while True:
    for i in range(0, password_count):
        password = ''
        for j in range(0, password_length):
            password_character = random.choice(characters)
            password = password + password_character
        print('The generated password is : ', password)
    repeat = input('Do you want to generate more passwrods?')
    if repeat == 'no' or 'No':
        break
