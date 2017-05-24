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


