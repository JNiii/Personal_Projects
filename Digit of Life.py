'''Digit of Life is a digit evaluated using somebody's birthday.
It's simple - you just need to sum all the digits of the date.
If the result contains more than one digit,
you have to repeat the addition until you get exactly one digit'''

bday = input('Please input your birthday in format MMDDYYYY: ')
bday_list = [int(i) for i in bday]
DoL = 0 #initial value
while len(bday_list) != 1:
    bday_sum = str(sum(bday_list))
    bday_list = [int(i) for i in bday_sum]
    DoL = int(bday_sum)

print("Your Digit of Life is: " + DoL)
