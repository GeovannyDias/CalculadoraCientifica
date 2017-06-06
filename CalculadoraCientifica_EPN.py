
##############################################################
######################CALCULADORA#############################

from tkinter import*
import math

cal = Tk()
op = ''
x =''
ver = False

cal.geometry("230x280+300+250")
cal.title('Calculator Científica - EPN')
cal.resizable(width=False, height=False)
operator = ''
text_Input = StringVar()
def reiniciar():
    ver=True
    op = ""
    operator1 = ""
    operator = ""

    
def otr(operator1):
    global op
    global ver
    ver = True
    op = operator1
    text_Input.set(operator1)
    
      
def BtnOperacion(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(op + operator)
    

def BorrarDatos():
    global operator
    operator1 = ''
    operator = ""
    text_Input.set("")
    op = ""
    ver = False

def btnResultado():
    global operator
    x = "sen("
    y = "cos("
    z = "tan("
    a = "cotan("
    b = "cec("
    c = "csc("
    if ver == True:
        if op == x:
            s=str(math.sin(math.radians(int(operator))))
            text_Input.set(s)
            operator = ""
        elif op ==y :
            s=str(math.cos(math.radians(int(operator))))
            text_Input.set(s)
            operator = ""
        elif op == z:
            s=str(math.tan(math.radians(int(operator))))
            text_Input.set(s)
            operator = ""
        elif op == a:
            s = str(math.atan(math.radians(int(operator))))
            text_Input.set(s)
            operator = ""
        elif op == b:
            s = str(math.acos(math.radians(int(operator))))
            text_Input.set(s)
            operator = ""
        elif op == c:
            s = str(math.asin(math.radians(int(operator))))
            text_Input.set(s)
            operator = ""
        
    else:
        s=str(eval(operator))
        text_Input.set(s)

        operator = ""
    

txt_Display = Entry(cal, textvariable = text_Input, bd = 20, insertwidth = 4).grid(columnspan=100)

####################################################################################################

btnaSie = Button(cal, bd =15 , text= 7, relief="groove",command=lambda:BtnOperacion(7)).grid(row=1,column=0)
btnOch = Button(cal, bd =15 , text= 8, relief="groove",command=lambda:BtnOperacion(8)).grid(row=1,column=1)
btnNue = Button(cal, bd =15 , text= 9, relief="groove",command=lambda:BtnOperacion(9)).grid(row=1,column=2)
btnast = Button(cal, bd =15 , text= '*',relief="groove", command=lambda:BtnOperacion('*')).grid(row=1,column=3)
btnDiv = Button(cal, bd =15 , text= '/', relief="groove",command=lambda:BtnOperacion('/')).grid(row=1,column=4)


####################################################################################################

btnCuat = Button(cal, bd =15 , text= 4, relief="groove",command=lambda:BtnOperacion(4)).grid(row=2,column=0)
btnCinc = Button(cal, bd =15 , text= 5, relief="groove",command=lambda:BtnOperacion(5)).grid(row=2,column=1)
btnSei = Button(cal, bd =15 , text= 6, relief="groove",command=lambda:BtnOperacion(6)).grid(row=2,column=2)
btnSum = Button(cal, bd =15 , text= '+',relief="groove", command=lambda:BtnOperacion('+')).grid(row=2,column=3)
btnClear = Button(cal, bd =15 , text= 'C', relief="groove",command=BorrarDatos).grid(row=2,column=4)

####################################################################################################

btnUn = Button(cal, bd =15 , text= 1, relief="groove",command=lambda:BtnOperacion(1)).grid(row=3,column=0)
btnDos = Button(cal, bd =15 , text= 2,relief="groove", command=lambda:BtnOperacion(2)).grid(row=3,column=1)
btnTres = Button(cal, bd =15 , text= 3,relief="groove", command=lambda:BtnOperacion(3)).grid(row=3,column=2)
btnRes = Button(cal, bd =15, text= '-',relief="groove",command=lambda:BtnOperacion('-')).grid(row=3,column=3)
btnPto = Button(cal, bd =15, text= '.',relief="groove", command=lambda:BtnOperacion('.')).grid(row=3,column=4)
btnCer = Button(cal, bd =9 , text= 0,relief="groove", command=lambda:BtnOperacion(0)).grid(row=4,column=0)

####################################################################################################
                                                                            
btnSen = Button(cal, bd =7 , text= 'sin(',relief="groove", command=lambda:otr('sen(')).grid(row=4,column=1)
btnCos = Button(cal, bd =7 , text= 'cos(',relief="groove", command=lambda:otr('cos(')).grid(row=4,column=2)
btnTan = Button(cal, bd =7 , text= 'tan(',relief="groove", command=lambda:otr('tan(')).grid(row=4,column=3)
btnIgual = Button(cal, bd =9.5, text= '=', relief="groove",command=btnResultado).grid(row=4,column=4)
cal.mainloop()


#LAS FUNCIONES SEN, COS, TAN, YA SE CALCULAN HAY QUE VALIDAR CUANDO CADA FUNCION TOMA VALOR DE
#0,90,180,270,360 PARA CADA UNA DE ELLAS, Y ADEMAS FALTA LA VALIDADCION DE QUE DESPUES DE INGRESAR
#UNA FUNCION TRIGONOMETRICA Y QUE DE EL RESULTADO, AL MOMETNO DE APLASTAR UN NUMERO NO MARQUE NUEVAMENETE LA FUNCION
#PARA QUE ENTIENDAN MEJOR PRIMERO EJECUTEN UNA FUNCION TRIGONOMETRICA, LUEGO UNA SUMA Y VERAN LO QUE PASA


