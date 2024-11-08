from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont

root = Tk()
root.title("Calculator")
helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")

firstNum = 0
secondNum = 0
oper = ""

def turnOff():
    exit()

def clear():
    inpt_result.delete(0, 'end')

def addNum(num):
    inpt_result.insert('end', num)

def operation(op):
    global firstNum, oper
    firstNum = inpt_result.get()
    isNum = False
    while isNum == False:
        try:
            firstNum = float(firstNum)
            isNum = True
        except ValueError:
            messagebox.showerror("Error!", "Invalid input!")
            return 0
    inpt_result.delete(0, 'end')
    oper = op


def result():
    global secondNum
    secondNum = inpt_result.get()
    isNum = False
    while isNum == False:
        try:
            secondNum = float(secondNum)
            isNum = True
        except ValueError:
            messagebox.showerror("Error!", "Invalid input!")
            return 0
    inpt_result.delete(0, 'end')
    if oper == "+":
        res = firstNum + secondNum
    elif oper == "-":
        res = firstNum - secondNum
    elif oper == "*":
        res = firstNum * secondNum
    elif oper == "/":
        res = firstNum / secondNum
    inpt_result.insert('end', res)

inpt_result = Entry(root, bg='#000000', fg='#ffffff', justify=RIGHT, width=10, font=helv36)
inpt_result.focus_set()
btn_off = Button(root, text="Off", width=2, font=helv36, bg='#e6001a', command=turnOff)
btn_clear = Button(root, text="C", width=2, font=helv36, bg='#ebed5d', command=clear)
btn_div = Button(root, text="/", width=2, font=helv36, bg='#ebed5d', command=lambda: operation("/"))
btn_mult = Button(root, text="*", width=2, font=helv36, bg='#ebed5d', command=lambda: operation("*"))
btn_sub = Button(root, text="-", width=2, font=helv36, bg='#ebed5d', command=lambda: operation("-"))
btn_add = Button(root, text="+", width=2, font=helv36, bg='#ebed5d', command=lambda: operation("+"))
btn_equ = Button(root, text="=", width=2, font=helv36, bg='#0057ff', command=result)
for i in range(0, 9):
    btn = Button(root, text=i+1, width=2, font=helv36, command=lambda i = i+1: addNum(i))
    btn.grid(row=2 if i < 3 else 3 if i < 6 else 4,
             column=0 if i % 3 == 0 else 1 if i % 3 == 1 else 2)
btn_zero = Button(root, text="0", width=2, font=helv36, command=lambda: addNum(0))
btn_zero.grid(column=1, row=5)

inpt_result.grid(column=0, row=0, columnspan=4)
btn_off.grid(column=0, row=1)
btn_clear.grid(column=1, row=1)
btn_div.grid(column=2, row=1)
btn_mult.grid(column=3, row=1)
btn_sub.grid(column=3, row=2)
btn_add.grid(column=3, row=3)
btn_equ.grid(column=3, row=4)

root.mainloop()
