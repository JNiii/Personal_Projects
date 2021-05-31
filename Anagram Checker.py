#Anagram Checker

count = 0
str_1 = sorted(list(input('Please enter first string: ').lower().replace(' ','')))
str_2 = sorted(list(input('Please enter second string: ').lower().replace(' ','')))
if str_1 != str_2:
    print('Not anagrams')
else:
    print('Anagrams')
