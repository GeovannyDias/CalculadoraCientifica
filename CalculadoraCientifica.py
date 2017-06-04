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

#Ivonne Vega
from tkinter import *

def bntClick(num):
    global operacion
    operacion=operacion + str(num)
    txt_Input.set(operacion)

tk =Tk()
tk.title('Calculadora')
operacion =''
txt_Input=StringVar()

txtDisplay = Entry(tk,textvariable=txt_Input, insertwidth=8).grid(columnspan=8)


    
btn1= Button(tk,text="1", command=lambda:bntClick(1)).grid(row=4, column=1)

btn2= Button(tk,text="2", command=lambda:bntClick(2)).grid(row=4, column=2)

btn3= Button(tk,text="3", command=lambda:bntClick(3)).grid(row=4, column=3)

btn4= Button(tk,text="4",command=lambda:bntClick(4)).grid(row=4, column=4)

btn5= Button(tk,text="5",command=lambda:bntClick(5)).grid(row=5, column=1)

btn6= Button(tk,text="6",command=lambda:bntClick(6)).grid(row=5, column=2)

btn7= Button(tk,text="7",command=lambda:bntClick(7)).grid(row=5, column=3)

btn8= Button(tk,text="8",command=lambda:bntClick(8)).grid(row=5, column=4)

btn9= Button(tk,text="9",command=lambda:bntClick(9)).grid(row=6, column=1)

btn0= Button(tk,text="0",command=lambda:bntClick(0)).grid(row=6, column=2)

btnSum= Button(tk,text="Sumar",command=lambda:bntClick(0))
btnSum.grid(row=8, column=1)

mainloop()

###############################################################################
#Fernanda Cordova
from tkinter import *


def btnClick(numeros):
    global operacion
    operacion = operacion + str(numeros)
    text_Input.set(operacion)


tk = Tk()
tk.title('calculadora')
operacion = ""
text_Input = StringVar()
txtDisplay = Entry(tk, textvariable=text_Input, bd=30, insertwidth=4).grid(columnspan=4)

btn1 = Button(tk, text=" 1 ", command=lambda: btnClick(1))
btn1.grid(row=1, column=1)

btn2 = Button(tk, text=" 2 ", command=lambda: btnClick(2))
btn2.grid(row=1, column=2)

btn3 = Button(tk, text=" 3 ", command=lambda: btnClick(3))
btn3.grid(row=1, column=3)

btn4 = Button(tk, text=" 4 ", command=lambda: btnClick(4))
btn4.grid(row=2, column=1)

btn5 = Button(tk, text=" 5 ", command=lambda: btnClick(5))
btn5.grid(row=2, column=2)

btn6 = Button(tk, text=" 6 ", command=lambda: btnClick(6))
btn6.grid(row=2, column=3)

btn7 = Button(tk, text=" 7 ", command=lambda: btnClick(7))
btn7.grid(row=3, column=1)

btn8 = Button(tk, text=" 8 ", command=lambda: btnClick(8))
btn8.grid(row=3, column=2)

btn9 = Button(tk, text=" 9 ", command=lambda: btnClick(9))
btn9.grid(row=3, column=3)

btn10 = Button(tk, text=" - ", command=lambda: btnClick("-"))
btn10.grid(row=4, column=1)

btn11 = Button(tk, text=" + ", command=lambda: btnClick(" + "))
btn11.grid(row=4, column=2)

btn12 = Button(tk, text=" = ", command=lambda: btnClick(" = "))
btn12.grid(row=4, column=3)
mainloop()
