from tkinter import PhotoImage, Tk, Label, Button, Entry, Frame
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from turtle import width
from matplotlib.font_manager import FontProperties



def NuevaReceta():
    new=Tk()
    new.title("Recetas")
    new.geometry("600x600")
    

    lbl=Label(new, text="Hi! Chef,  Listo para escribir La Nueva Receta Secreta", fg='black',font='Algerian')
    lbl.place(relx=.05,rely=.03, relheight=.1, relwidth=.9 )
    
    scrolledtext1=st.ScrolledText(new, width=80, height=20, bg='#CABEDB')
    scrolledtext1.grid(column=0,row=0, padx=5, pady=65)
    def guardar():
        nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(scrolledtext1.get("1.0",'end'))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")
         
    boton=Button(new, text="Guardar",bg='white', fg='blue', command=guardar)
    boton.place(relx=.6,rely=.8, relheight=.08, relwidth=.3 )
    

    new.mainloop()
    

if __name__ == '__main__':
    NuevaReceta()



