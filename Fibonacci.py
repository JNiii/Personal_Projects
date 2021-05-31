#Fibonacci Sequence

fib = [0,1,1,] #initialize values
arg = 3 #3 elements inside the fib sequence

def fibonacci(elem):
    elem_check,  length_check = False, False
    while not elem_check:
        try:
            num = int(input(elem))
            elem_check = True
        except ValueError:
            print('Wrong input. Please input numbers only')
    while not length_check:
        try:
            length = int(input('How long in the fibonacci sequence should I search? '))
            length_check = True
        except:
            print('Wrong input. Please input 5-100 only.')
    i = 3
    while i <= length:
        fib.append(fib[i-1]+fib[i-2])
        i += 1
    print(fib)
    if num in fib:
        print(num, 'is in fibonacci sequence with', length, 'elements')
        print(num, 'is the', str(fib.index(num)+1) +'th element', 'in the sequence')
    else:
        print(num, 'is not in fibonacci sequence with', length, 'elements')

v = fibonacci('Input number to search on Fibonacci Sequence: ')
