#Leap Year
'''
A program that checks if a year is a Leap Year
'''

def check_leap(yr):
    check = False
    while not check:
        try:
            num = int(input(yr))
            check = True
        except ValueError:
            print('Wrong input')
    if num <= 1582:
        print(num, 'is not a leap year')
    elif num % 4 == 0:
        if num % 400 == 0:
            print(num, 'is a leap year')
        elif num % 100 == 0:
            print(num, 'is not a leap year')
        else:
            print(num, 'is a leap year')
    elif num % 4 != 0:
        print(num, 'is not a leap year')

v = check_leap('Input a year: ')
