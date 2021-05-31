import sys
import random

letter = ''
print('Welcome to Guess the word game!')
name = input('Please tell me your name: ')
word_list = ['apple','beetle','geek','razor','battery']

def start_game():
    print('You have 5 lives to guess each word')
    guess_word = random.choice(word_list)
    blank_str = ' '.join(['_' for _ in guess_word])
    blank_list = ['_' for _ in guess_word]
    print(blank_str)
    no_guess = 5
    index_list = []
    count = 0
    while no_guess > 0:
        letter = input('Please type your guess letter: ').lower()
        if letter in guess_word:
            print('Your guess is correct')
            for i in guess_word:
                if i == letter:
                    index_list.append(count)
                    count += 1
                else:
                    count += 1
            print(index_list)
            count = 0
            for i in index_list:
                blank_list[i] = letter
            blank_str = ' '.join(blank_list)
            index_list = []
            print(blank_str)
            if blank_list == list(guess_word):
                print('You\'ve won',name + '!')
                break
        elif letter not in guess_word:
            no_guess -= 1
            print('Incorrect guess, no. of tries left =',no_guess)
            if no_guess == 0:
                print('You lose!')
                break

if input('Would you like to play?(Y/N) ').lower() == 'y':
    start_game()
else:
    sys.exit()

