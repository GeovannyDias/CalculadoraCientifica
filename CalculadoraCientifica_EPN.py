from tkinter import*
root = Tk()
root.geometry("200x300")
root.title('Calculator Científica - EPN')

fr1 = Frame(root)
fr1.pack(side = TOP)
fr2 = Frame(root)
fr2.pack()

operador = ''
text_Input = StringVar()


def btnClick(variable):
    global operador
    operador += str(variable)
    text_Input.set(operador)

def btnClearDisplay():
    global operador
    operador=""
    text_Input.set("")

def btnResultado():
    global operador
    resultado = str(eval(operador))
    text_Input.set(resultado)
    operador = resultado


txt_Display = Entry(fr1,textvariable=text_Input, bd = 30, insertwidth = 4).grid(columnspan=4)
btn = Button(fr2,bd = 10, text = '*', command=lambda:btnClick('*')).grid(row=0,column=3)
btn = Button(fr2,bd = 10, text = '+', command=lambda:btnClick('+')).grid(row=1,column=3)
btn = Button(fr2,bd = 10, text = '-', command=lambda:btnClick('-')).grid(row=2,column=3)
btn = Button(fr2,bd = 10, text = '/', command=lambda:btnClick('/')).grid(row=3,column=3)

btn = Button(fr2,bd = 10, text = '7', command=lambda:btnClick(7)).grid(row=0,column=0)
btn = Button(fr2,bd = 10, text = '8', command=lambda:btnClick(8)).grid(row=0,column=1)
btn = Button(fr2,bd = 10, text = '9', command=lambda:btnClick(9)).grid(row=0,column=2)
btn = Button(fr2,bd = 10, text = '4', command=lambda:btnClick(4)).grid(row=1,column=0)
btn = Button(fr2,bd = 10, text = '5', command=lambda:btnClick(5)).grid(row=1,column=1)
btn = Button(fr2,bd = 10, text = '6', command=lambda:btnClick(6)).grid(row=1,column=2)
btn = Button(fr2,bd = 10, text = '3', command=lambda:btnClick(3)).grid(row=2,column=0)
btn = Button(fr2,bd = 10, text = '2', command=lambda:btnClick(2)).grid(row=2,column=1)
btn = Button(fr2,bd = 10, text = '1', command=lambda:btnClick(1)).grid(row=2,column=2)
btn = Button(fr2,bd = 10, text = '').grid(row=3,column=0)
btn = Button(fr2,bd = 10, text = '0', command=lambda:btnClick(0)).grid(row=3,column=1)
btn = Button(fr2,bd = 10, text = '.', command=lambda:btnClick('.')).grid(row=3,column=2)

btn = Button(fr2,bd = 10, text = '', command=lambda:btnClick('')).grid(row=4,column=0)
btn = Button(fr2,bd = 10, text = '', command=lambda:btnClick('')).grid(row=4,column=1)
btn = Button(fr2,bd = 10, text = 'C', command=btnClearDisplay).grid(row=4,column=2)
btn = Button(fr2,bd = 10, text = '=', command=lambda:btnResultado()).grid(row=4,column=3)

root.mainloop()
