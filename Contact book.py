#Contact Book
#A program that simulates a contact book

import sys
response = ''
book = {}
print('Welcome to your personal contact book')

def respond():
    global response
    print('What would you like to do?')
    response = input('Save?\nSearch?\nDelete?\nNothing?\n')
    compare()
    
def compare():
    if response == 'Save':
        save()
    elif response == 'Search':
        csearch()
    elif response == 'Delete':
        delete()
    elif response == 'Nothing':
        print('Thank you!')
        sys.exit()

def save():
    state = True
    while state:
        book.update({input('Please input contact name: '):input('Please input contact number: ')})
        if input('Would like to add more?(Y/N)\n') == 'Y':
            state = True
        else:
            state = False
    print(book)
    respond()
    
def csearch():
    cname = input('Please input a contact name to be searched:\n')
    if cname not in book:
        print(cname,'is not a saved contact.')
    else:
        print(cname, 'has a number', book[cname])
    respond()

def delete():
    cname = input('Input contact name to be deleted: ')
    if cname not in book:
        print(cname,'is not a saved contact')
    else:
        del book[cname]
        print(cname, 'is deleted from your contact list')
        print('Your current contact book is:', book)
    respond()
    
respond()
