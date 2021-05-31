print('Welcome to Mad Libs creator!')
name = input('Please tell me your name human.. ')
print('Hello', name, '!. Let\'s start')
color = []

for i in range(3):
    color.append(input('Please enter color: '))


print('The Sky is', color[0])
print('The Ocean is', color[1])
print('Mountains are', color[2])
