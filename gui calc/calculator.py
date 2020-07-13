from tkinter import *

root = Tk()
root.title('Calculator')
root.iconbitmap('C:/Users/sound/PycharmProjectsTkinter/calcicon.ico')
root.geometry('288x446')
root.resizable(width=0, height=0)
root.configure(bg='Grey')
# getting value
e = Entry(root, width=45, borderwidth=5, bg='white')
e.grid(row=0, column=0, columnspan=3)


# button operations
def myclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clickAdd():
    first_num = e.get()
    global f_num
    global math
    math = "Addition"
    f_num = int(first_num)
    e.delete(0, END)


def clickSub():
    first_num = e.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = int(first_num)
    e.delete(0, END)


def clickDiv():
    first_num = e.get()
    global f_num
    global math
    math = "Division"
    f_num = int(first_num)
    e.delete(0, END)


def clickMul():
    first_num = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = int(first_num)
    e.delete(0, END)


def clickMod():
    first_num = e.get()
    global f_num
    global math
    math = "Modulo"
    f_num = int(first_num)
    e.delete(0, END)


def clickEqual():
    if math == "Addition":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num + int(second_num))
    if math == "Subtraction":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num - int(second_num))
    if math == "Division":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num / int(second_num))
    if math == "Modulo":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num % int(second_num))
    if math == "Multiplication":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num * int(second_num))

def clickClear():
    e.delete(0, END)


# creating buttons
num7 = Button(root, text='7', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=lambda: myclick(7))
num8 = Button(root, text='8', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=lambda: myclick(8))
num9 = Button(root, text='9', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=lambda: myclick(9))
num4 = Button(root, text='4', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=lambda: myclick(4))
num5 = Button(root, text='5', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=lambda: myclick(5))
num6 = Button(root, text='6', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=lambda: myclick(6))
num1 = Button(root, text='1', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=lambda: myclick(1))
num2 = Button(root, text='2', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=lambda: myclick(2))
num3 = Button(root, text='3', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=lambda: myclick(3))
num0 = Button(root, text='0', borderwidth=4, padx=39, pady=25, bg='grey10', fg='OrangeRed', command=lambda: myclick(0))

# operations
clear = Button(root, text='CLEAR', borderwidth=6, padx=71, pady=23, bg='grey10', fg='OrangeRed', command=clickClear)
add = Button(root, text='+', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=clickAdd)
button_equal = Button(root, text='=', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=clickEqual)
sub = Button(root, text='-', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=clickSub)
mul = Button(root, text='*', borderwidth=4, padx=39, pady=20, bg='grey10', fg='OrangeRed', command=clickMul)
div = Button(root, text='/', borderwidth=4, padx=38, pady=20, bg='grey10', fg='OrangeRed', command=clickDiv)
mod = Button(root, text='%', borderwidth=4, padx=37, pady=20, bg='grey10', fg='OrangeRed', command=clickMod)

# shoving into screen
num7.grid(row=1, column=0)
num8.grid(row=1, column=1)
num9.grid(row=1, column=2)
num4.grid(row=2, column=0)
num5.grid(row=2, column=1)
num6.grid(row=2, column=2)
num1.grid(row=3, column=0)
num2.grid(row=3, column=1)
num3.grid(row=3, column=2)
num0.grid(row=4, column=0)
clear.grid(row=4, column=1, columnspan=2)
add.grid(row=5, column=0)
button_equal.grid(row=5, column=2)
sub.grid(row=5, column=1)
mul.grid(row=6, column=0)
div.grid(row=6, column=1)
mod.grid(row=6, column=2)

root.mainloop()
