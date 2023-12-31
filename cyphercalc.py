#TEC-Labs Calculator
from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("DigiLabs: Calculator")
root.configure(background="gray60")
root.resizable(width=False,height=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

#TEC-Labs class for calculator

class Calc:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.ip_val = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self,num):
        self.result = False
        first_num = txtDisplay.get()
        second_num = str(num)

        if self.ip_val:
            self.current = second_num
            self.ip_val = False
        else:
            if second_num == '.':
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def valid_function(self):
        if self.op == 'add':
            self.total += self.current
        elif self.op == 'sub':
            self.total -= self.current
        elif self.op == 'mul':
            self.total *= self.current
        elif self.op == 'div':
            try:
                self.total /= self.current
            except ZeroDivisionError:
                self.total = "ZeroDivisionError"
        elif self.op == 'mod':
            self.total %= self.current
        elif self.op == 'pow':
            self.total = self.total ** self.current
        elif self.op == 'com':
            self.total = math.comb(int(self.total), int(self.current))
        elif self.op == 'per':
            self.total = math.perm(int(self.total), int(self.current))
        elif self.op == 'fac':
            self.total = math.factorial(int(self.total))
        elif self.op == 'b':
            binary = bin(int(self.total))
            self.total = binary[2:]
        elif self.op == 'o':
            octal = oct(int(self.total))
            self.total = octal[2:]
        elif self.op == 'h':
            hexa = hex(int(self.total))
            self.total = hexa[2:]
        elif self.op == 'g':
            self.total = math.gcd(int(self.total),int(self.current))
        elif self.op == 'f':
            self.total = math.frexp(self.total)


        self.ip_val = True
        self.check_sum = False
        self.display(self.total)

    def operation(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.ip_val = True
        self.check_sum = True
        self.op = op
        self.result = False

#TEC-Labs display
    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)

    def clear_entry(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.ip_val = True

    def clear_all(self):
        self.clear_entry()
        self.total = 0

#TEC-Labs scientific
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def PM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def sq_rt(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def ln(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def asin(self):
        self.result = False
        self.current = math.asin(math.radians(float(txtDisplay.get())))
        self.display(math.degrees(self.current))

    def acos(self):
        self.result = False
        self.current = math.acos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def atan(self):
        self.result = False
        self.current = math.atan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def radians(self):
        self.result = False
        self.current = math.radians(float(txtDisplay.get()))
        self.display(self.current)



res = Calc()


#TEC-Labs Graphics for the calculator

txtDisplay = Entry(calc,font=('arial',20,'bold'),bd=30,bg='gray60',width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,'0')

numpad = '789456123'
i=0
btn = []

for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('arial',20,'bold'),bd=4,text=numpad[i],bg="darkcyan"))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]['command'] = lambda x = numpad [i]:res.numberEnter(x)
        i+=1

#TEC-Labs standard calculator
Button(calc,text=chr(67),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="cyan",command = res.clear_entry).grid(row=1,column=0,pady=1)
Button(calc,text=chr(67)+chr(69),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="skyblue",command = res.clear_all).grid(row=1,column=1,pady=1)
Button(calc,text=u'\u221A',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="blue",command = res.sq_rt).grid(row=1,column=2,pady=1)
Button(calc,text='+',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="blue",command = lambda: res.operation('add')).grid(row=1,column=3,pady=1)

Button(calc,text='-',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="blue",command = lambda: res.operation('sub')).grid(row=2,column=3,pady=1)
Button(calc,text='*',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="blue",command = lambda: res.operation('mul')).grid(row=3,column=3,pady=1)
Button(calc,text='/',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="blue",command = lambda: res.operation('div')).grid(row=4,column=3,pady=1)
Button(calc,text='=',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="blue",command = res.sum_of_total).grid(row=5,column=3,pady=1)

Button(calc,text='.',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="blue",command = lambda: res.numberEnter('.')).grid(row=5,column=0,pady=1)
Button(calc,text='0',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="darkcyan",command = lambda: res.numberEnter(0)).grid(row=5,column=1,pady=1)
Button(calc,text=chr(177),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="blue",command = res.PM).grid(row=5,column=2,pady=1)

#Scientific
Button(calc,text='^',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = lambda: res.operation('pow')).grid(row=0,column=4,pady=1)
Button(calc,text='nCr',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = lambda: res.operation('com')).grid(row=0,column=5,pady=1)
Button(calc,text='nPr',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = lambda: res.operation('per')).grid(row=0,column=6,pady=1)

Button(calc,text=u'\u03C0',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.pi).grid(row=1,column=4,pady=1)
Button(calc,text='sin',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.sin).grid(row=2,column=4,pady=1)
Button(calc,text='cos',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.cos).grid(row=2,column=5,pady=1)
Button(calc,text='tan',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.tan).grid(row=2,column=6,pady=1)

Button(calc,text='log',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.log).grid(row=4,column=4,pady=1)
Button(calc,text='asin',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.asin).grid(row=3,column=4,pady=1)
Button(calc,text='acos',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.acos).grid(row=3,column=5,pady=1)
Button(calc,text='atan',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.atan).grid(row=3,column=6,pady=1)

Button(calc,text='ln',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.ln).grid(row=4,column=5,pady=1)
Button(calc,text='exp',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.exp).grid(row=1,column=6,pady=1)
Button(calc,text='mod',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = lambda: res.operation('mod')).grid(row=5,column=6,pady=1)
Button(calc,text='e',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.e).grid(row=1,column=5,pady=1)

Button(calc,text='log2',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.log2).grid(row=4,column=6,pady=1)
Button(calc,text='deg',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.degrees).grid(row=5,column=4,pady=1)
Button(calc,text='rad',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = res.radians).grid(row=5,column=5,pady=1)

#TEC-Labs last row
Button(calc,text='!',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = lambda: res.operation('fac')).grid(row=0,column=7,pady=1)
Button(calc,text='bin',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = lambda: res.operation('b')).grid(row=1,column=7,pady=1)
Button(calc,text='oct',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = lambda: res.operation('o')).grid(row=2,column=7,pady=1)
Button(calc,text='hex',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = lambda: res.operation('h')).grid(row=3,column=7,pady=1)
Button(calc,text='frexp',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = lambda: res.operation('f')).grid(row=4,column=7,pady=1)
Button(calc,text='GCD',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command = lambda: res.operation('g')).grid(row=5,column=7,pady=1)

#TEC-Labs menu

def Exit():
    if tkinter.messagebox.askyesno("Calculator","Confirm if you want to quit") >0 :
        root.destroy()
        return


def Sci():
    root.resizable(width=False,height=False)
    root.geometry("950x568+0+0")


def Std():
    root.resizable(width=False,height=False)
    root.geometry("480x568+0+0")

menubar = Menu(calc)

file_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Standard",command=Std)
file_menu.add_command(label="Scientific",command=Sci)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=Exit)

root.config(menu=menubar)
root.mainloop()