#Simple Calculator GUI using Tkinter


from tkinter import *

first_num, op = '', ''

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width = 30, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3)

def put_num(n):
    cur_num = e.get()
    e.delete(0, END)
    e.insert(0 ,str(cur_num) + str(n))
    
def add_num():
    global first_num, op
    first_num = str(e.get())
    e.delete(0, END)
    op = '+'
def equal():
    second_num = str(e.get())
    e.delete(0, END)
    total = first_num + op + second_num
    total = str(eval(total))
    e.insert(0, total)
      
def clear_num():
    
    e.delete(0, END)
    
def sub_num():
    global first_num, op
    first_num = str(e.get())
    e.delete(0, END)
    op = '-'
def div_num():
    global first_num, op
    first_num = str(e.get())
    e.delete(0, END)
    op = '/'
def mult_num():
    global first_num, op
    first_num = str(e.get())
    e.delete(0, END)
    op = '*'




button_1 = Button(root, text = '1',padx = 25, pady = 10, command = lambda: put_num(1))
button_2 = Button(root, text = '2',padx = 25, pady = 10, command = lambda: put_num(2))
button_3 = Button(root, text = '3',padx = 25, pady = 10, command = lambda: put_num(3))
button_4 = Button(root, text = '4',padx = 25, pady = 10, command = lambda: put_num(4))
button_5 = Button(root, text = '5',padx = 25, pady = 10, command = lambda: put_num(5))
button_6 = Button(root, text = '6',padx = 25, pady = 10, command = lambda: put_num(6))
button_7 = Button(root, text = '7',padx = 25, pady = 10, command = lambda: put_num(7))
button_8 = Button(root, text = '8',padx = 25, pady = 10, command = lambda: put_num(8))
button_9 = Button(root, text = '9',padx = 25, pady = 10, command = lambda: put_num(9))
button_0 = Button(root, text = '0',padx = 25, pady = 10, command = lambda: put_num(0))
button_add = Button(root, text = '+',padx = 25, pady = 10, command = add_num)
button_sub = Button(root, text = '-',padx = 25, pady = 10, command = sub_num)
button_div = Button(root, text = '/',padx = 25, pady = 10, command = div_num)
button_mult = Button(root, text = '*',padx = 25, pady = 10, command = mult_num)
button_equals = Button(root, text = '=',padx = 65, pady = 10, command = equal)
button_clear = Button(root, text = 'Clr',padx = 20, pady = 10, command = clear_num, bg = 'red')

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_0.grid(row = 4, column = 0)
button_add.grid(row = 1, column = 4)
button_sub.grid(row = 2, column = 4)
button_div.grid(row = 3, column = 4)
button_mult.grid(row = 4, column = 4)
button_equals.grid(row = 4, column = 1, columnspan = 2)
button_clear.grid(row = 0, column = 4)



root.mainloop()
