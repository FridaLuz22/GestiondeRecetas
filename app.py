from cProfile import label
from hashlib import new
from tkinter import PhotoImage, Tk, Label, Button, Entry, Frame
import tkinter
from click import command
from matplotlib.pyplot import text
from numpy import size


import nuevasrecetas

def recet():
    fichero=open('receta.txt')
    print(fichero.read())
    fichero.close()
    
def newventana2():
    archi2=open('receta2.txt')
    print(archi2.read())

def Nreceta():
    nuevasrecetas.NuevaReceta()
    



ventana=Tk()
ventana.title("Aplicacion")
ventana.geometry("600x600")

lbl=Label(ventana, text="Hi! Chefs", fg='black', font='Algerian')
lbl.place(relx=.05,rely=.03, relheight=.1, relwidth=.9 )

buscador=Entry(ventana, text="Buscar", fg='grey')
buscador.place(relx=.05,rely=.15, relheight=.04, relwidth=.5)

BuscarBoton=Button(ventana, text="Buscar", fg='black',bg='#55D48F')
BuscarBoton.place(relx=.6,rely=.15, relheight=.04, relwidth=.08)

crearBoton=Button(ventana, text="Crear Nueva Receta", fg='black',bg='turquoise', command=Nreceta)
crearBoton.place(relx=.05,rely=.22, relheight=.04, relwidth=.2)

frame=Frame(ventana, bg='pink')
frame.place(relx=.06,rely=.3, relheight=.6, relwidth=.4)
frame2=Frame(ventana, bg='pink')
frame2.place(relx=.53,rely=.3, relheight=.6, relwidth=.4)

subframe1=Frame(frame, bg="turquoise")
subframe1.place(relx=.05,rely=.03, relheight=.65, relwidth=.9)
subframe2=Frame(frame2, bg="turquoise")
subframe2.place(relx=.05,rely=.03, relheight=.65, relwidth=.9)

lblframe=Label(frame, text="Estofado de Res", fg='grey', font='Rockwell')
lblframe.place(relx=.05,rely=.7, relheight=.1, relwidth=.9 )
lblframe2=Label(frame2, text="Aji de Gallina", fg='grey', font='Rockwell')
lblframe2.place(relx=.05,rely=.7 , relheight=.1, relwidth=.9 )

BotonFrame=Button(frame, text="Ver Receta", fg='black',bg='#55D48F',command=recet)
BotonFrame.place(relx=.5,rely=.85, relheight=.1, relwidth=.4)
BotonFrame2=Button(frame2, text="Ver Receta", fg='black',bg='#55D48F', command=newventana2)
BotonFrame2.place(relx=.5,rely=.85, relheight=.1, relwidth=.4)


ventana.mainloop()

