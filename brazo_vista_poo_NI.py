# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
from tkinter import messagebox
class vistaRB:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("BRAZO ROBOTICO")
        self.etiqueta1=tk.Label(self.ventana,text="BRAZO ROBOTICO ")
        self.etiqueta1.grid(row=0,column=0,columnspan=5,padx=7,pady=7)  
        self.etiqueta2=tk.Label(self.ventana,text="Datos de entrada ")
        self.etiqueta2.grid(row=1,column=0,columnspan=2,padx=1,pady=1)
        ##datos de entrada 
        self.etiqueta3=tk.Label(self.ventana,text="X")
        self.etiqueta3.grid(row=2,column=0,columnspan=2,padx=1,pady=1)
        self.etiqueta4=tk.Label(self.ventana,text="Y")
        self.etiqueta4.grid(row=3,column=0,columnspan=2,padx=1,pady=1)
        self.etiqueta5=tk.Label(self.ventana,text="Z")
        self.etiqueta5.grid(row=4,column=0,columnspan=2,padx=1,pady=1)
        ## ENTRY PARA VALORES DE ENTRADA 
        self.valorx=tk.Entry(self.ventana)
        self.valorx.grid(row=2,column=3,padx=2,pady=2)
        self.valory=tk.Entry(self.ventana)
        self.valory.grid(row=3,column=3,padx=2,pady=2)
        self.valorz=tk.Entry(self.ventana)
        self.valorz.grid(row=4,column=3,padx=2,pady=2)
        ##orientacion 
        self.etiqueta6=tk.Label(text="ingrese la orientacion: ")
        self.etiqueta6.grid(row=5,column=0,columnspan=3,padx=1,pady=1)
        self.orientacion=tk.Entry()
        self.orientacion.grid(row=5,column=3,columnspan=3,padx=1,pady=1)
        ##velocidad
        self.etiqueta7=tk.Label(text="ingrese la velocidd")
        self.etiqueta7.grid(row=6,column=0,columnspan=3,padx=1,pady=1)
        self.velocidad=tk.Entry()
        self.velocidad.grid(row=6,column=3,columnspan=3,padx=1,pady=1)
        ##ACEPTAR
        self.guardar=tk.Button(self.ventana,text="GUARDAR",command=lambda:self.get_user_input)
        self.guardar.grid(row=7,column=0,columnspan=4,padx=1,pady=1)  
        self.mostrar=tk.Button(self.ventana,text="MOSTRAR",command=lambda:self.set_user_output(x))
        self.mostrar.grid(row=8,column=0,columnspan=4,padx=1,pady=1)  
        self.ventana.mainloop()
    def get_user_input(self):
        global x,y,z
        x=self.valorx.get()
        y=self.valory.get()
        z=self.valorz.get()
        orient=self.orientacion.get()
        velo=self.velocidad.get()
        return x,y,z,orient,velo
    def set_user_output(self,x):
        messagebox.showinfo("salida de datos ", 
                            "(posicion: {x})")
        
        
    
vista1=vistaRB()
