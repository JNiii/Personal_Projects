from random import randint
import sys

print('Welcome to Dice Rolling Simulator')
print('''Would you like to proceed..
        Yes or No?''')
decision = input()
state = True

if decision.lower() == 'yes':
    while state:
        print('You rolled number',randint(1,6))
        print('''Would you like to roll again?
        Yes or No?''')
        decision = input()
        if decision.lower() == 'no':
            break
        else:
            state = True
print('Thank you for playing')
