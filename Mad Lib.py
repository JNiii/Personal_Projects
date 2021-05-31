#Simple mad libs creator

print('Welcome to Mad Libs creator!')
name = input('Please tell me your name: ')
print('Hello', name, '!. Let\'s start')
color = []

for i in range(3):
    color.append(input('Please enter color: '))


print('The Sky is {}.\nThe Ocean is {}.\nMountains are {}.'.format(color[0],color[1],color[2]))
