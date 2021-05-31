#Program that checks if an entered string is a palindrome
print('WELCOME TO PALINDROME CHECKER!')
in_str = input('Please input a sentence: ').lower()
in_str = list(in_str.replace(' ',''))
rev_str = in_str[::-1]

if in_str == rev_str:
    print('String is a palindrome')
else:
    print('String is not a palindrome')
