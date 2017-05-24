from tkinter import*

tem1 = 0
tem2 = 0
res = 0
    

def fun1():
    global tem1
    global tem2
    if tem1 > 0 :
        tem2 = 1
        suma(tem2)
    else:
        tem1 = 1
        suma(tem1)


        
    
def fun2():
    global tem1
    global tem2
    if tem1 > 0:
        tem2 = 2
        suma(tem2)
    else:
        tem1 = 2
        suma(tem1)


        
def suma(valor):
    global tem1
    global tem2
    global res
    
    res +=valor
    


def resultado():
    print(res)
        

def botones():
    btn1 = Button(tk, text = ' 1 ', command = fun1)
    btn1.grid(row=1, column=1)

    btn2 = Button(tk, text = ' 2 ', command = fun2)
    btn2.grid(row=1, column=2)

    btn1 = Button(tk, text = ' 3 ')
    btn1.grid(row=1, column=3)

    btn2 = Button(tk, text = ' 4 ')
    btn2.grid(row=2, column=1)

    btn1 = Button(tk, text = ' 5 ')
    btn1.grid(row=2, column=2)

    btn2 = Button(tk, text = ' 6 ')
    btn2.grid(row=2, column=3)

    btn1 = Button(tk, text = ' 7 ')
    btn1.grid(row=3, column=1)

    btn2 = Button(tk, text = ' 8 ')
    btn2.grid(row=3, column=2)

    btn1 = Button(tk, text = ' 9 ')
    btn1.grid(row=3, column=3)

    btn2 = Button(tk, text = ' 0 ')
    btn2.grid(row=4, column=1)

    btn1 = Button(tk, text = ' + ', command = suma)
    btn1.grid(row=4, column=2)

    btn2 = Button(tk, text = ' - ', command = resultado)
    btn2.grid(row=4, column=3)

    btn1 = Button(tk, text = ' = ', command = resultado)
    btn1.grid(row=5, column=2)


    




tk = Tk()
botones()

#mainloop()#Bucle de todo el codigo

########################################################################
#####################DAVID CASA CODIGO CALCULADORA######################


from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

cal = Tk()
cal.title('calculator')
operator = ''
text_Input = StringVar()


txt_Display = Entry(cal,textvariable=text_Input, bd = 30, insertwidth = 4,
    ).grid(columnspan=4)
btnast = Button(cal,bd = 10, text = '*', command=lambda:btnClick('*')).grid(row=1,column=0)
btn = Button(cal,bd = 10, text = '+', command=lambda:btnClick('+')).grid(row=1,column=1)
btn7 = Button(cal,bd = 10, text = '-', command=lambda:btnClick('-')).grid(row=1,column=2)
btn7 = Button(cal,bd = 10, text = '7', command=lambda:btnClick(9)).grid(row=2,column=0)
btn7 = Button(cal,bd = 10, text = '8', command=lambda:btnClick(8)).grid(row=2,column=1)
btn7 = Button(cal,bd = 10, text = '9', command=lambda:btnClick(7)).grid(row=2,column=2)
btn7 = Button(cal,bd = 10, text = '4', command=lambda:btnClick(6)).grid(row=3,column=0)
btn7 = Button(cal,bd = 10, text = '5', command=lambda:btnClick(5)).grid(row=3,column=1)
btn7 = Button(cal,bd = 10, text = '6', command=lambda:btnClick(4)).grid(row=3,column=2)
btn7 = Button(cal,bd = 10, text = '1', command=lambda:btnClick(3)).grid(row=4,column=0)
btn7 = Button(cal,bd = 10, text = '2', command=lambda:btnClick(2)).grid(row=4,column=1)
btn7 = Button(cal,bd = 10, text = '3', command=lambda:btnClick(1)).grid(row=4,column=2)
btn7 = Button(cal,bd = 10, text = '0', command=lambda:btnClick(0)).grid(row=4,column=2)
btn7 = Button(cal,bd = 10, text = 'C', command=btnClearDisplay).grid(row=1,column=3)
btn7 = Button(cal,bd = 10, text = '=', command=lambda:btnClick(1)).grid(row=4,column=2)


cal.mainloop()


