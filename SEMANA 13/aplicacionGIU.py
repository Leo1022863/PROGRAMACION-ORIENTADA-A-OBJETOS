import tkinter as tk
from tkinter import ttk

def agregar_elemento():
    elemento = entrada.get()
    if elemento:
        lista.insert(tk.END, elemento)
        entrada.delete(0, tk.END)

def limpiar_lista():
    lista.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Lista de Elementos")
ventana.geometry("400x300")  # Establece el tamaño de la ventana

# Componentes
etiqueta = tk.Label(ventana, text="Ingrese un dato:")  #LABEL
etiqueta.pack()

entrada = tk.Entry(ventana) #CAMPO DE TEXTO
entrada.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento) #BOTON
boton_agregar.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack()

lista = tk.Listbox(ventana) #TABLA PARA MOSTRAR DE DATOS
lista.pack()

ventana.mainloop()