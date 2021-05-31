from random import randint

print('Welcome to Number Guessing Game Human!')
name = input('Please tell me your name: ')
print('Hello',name,'!. Please select difficulty below.')
print('Easy')
print('Medium')
print('Hard')
difficulty = input()
tries = 0
if difficulty == 'Easy':
    a, b = 1, 10
    guess = 3
elif difficulty == 'Medium':
    a, b = 1, 100
    guess = 5
elif difficulty == 'Hard':
    a, b = 1, 1000
    guess = 8
number = randint(a, b)

while tries < guess:
    #GET INPUT
    print('What is your guess?')
    num = int(input())
    tries += 1
    if num == number:
        print('Your guess is correct!')
        print('Naglaing ka metten. Sana all')
        break
    elif tries - guess == 0:
        print('The correct answer is',number,'.')
        print('Ay shunga!')
        break
    elif num != number:
        print('You have',guess-tries,'guess left.')
