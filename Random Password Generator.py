#Random Password Generator
import sys, random
print('Welcome to RPG')
state = False

def gen_pass(name):
    #randomized/scramble letters
    old_pass = list(name)
    index = len(name)
    new_pass = ''
    for i in range(len(name)):
        randnum = random.randint(0,index) - 1
        letter = old_pass[randnum]
        new_pass += letter
        num = old_pass.index(letter)
        del old_pass[num]
        index = index - 1
    print('The password generated is: ',new_pass)
    
while not state:
    resp = input('Would you like to generate a password? (Y/N) \n')
    if resp == 'Y':
        state = True
        gen_pass(input('Input words to be randomized: \n'))
    elif resp == 'N':
        state = False
        print('Thank you for your patronage!')
        sys.exit()
    else:
        print('Wrong Response')
