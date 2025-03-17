import tkinter as tk
from tkinter import messagebox #importa la biblioteca
from tkinter import ttk

from clase_usuario import clase_usuario

lista_usuario = clase_usuario()

def agregar_usuario(nombre, correo, contrasenia)
    lista_usuario.agregar_usuario(nombre, correo, contrasenia)
    messagebox.showinfo("Informacion","Usuarioa agregado correctamente")
    tabla.insert("","end", values=(nombre, correo, contrasenia))
    entrada_contrasenia.delete(0, tk.END)




ventana = tk.Tk()  # inicializar la ventana principal

ventana.title("Ingreso de usuarios")   # Establece el titulo de la ventana
ventana.geometry("400x300")  # Establece el tamaño de la ventana
ventana.configure(bg = "lightblue")  # Establece el color de fondo de la ventana


#Etiquetas 

#nombre de usuario
etiqueta_nombre = tk.Label(ventana, text="Nombre de usuario:") #Crea una eitqueta con el texto nombre
etiqueta_nombre.pack(pady=5)
#caja de tecto => Entradas
etiqueta_nommbre = tk.Entry(ventana, width=30).pack(pady=5)


#contrasenia
etiqueta_contrasenia = tk.Label(ventana, text="Ingrese su contraseña:") #Crea una eitqueta con el texto nombre
etiqueta_contrasenia.pack(pady=5)
#caja de tecto => Entradas
etiqueta_contrasenia = tk.Entry(ventana, width=30).pack(pady=5)



#correo
etiqueta_correo = tk.Label(ventana, text="Ingrese su correo:") #Crea una eitqueta con el texto nombre
etiqueta_correo.pack(pady=5)
#caja de tecto => Entradas
etiqueta_correo = tk.Entry(ventana, width=30).pack(pady=5)



btn_guardar =tk.Button(ventana, text="Guardar").pack(pady=5)
btn_salir =tk.Button(ventana, text="Salir").pack(pady=5)
btn_editar =tk.Button(ventana, text="Editar").pack(pady=5)
btn_cancelar =tk.Button(ventana, text="Cancelar").pack(pady=5)


tabla = ttk.Treeview(ventana, columns=("Nombre","Correo","Contrasenia"))
tabla.heading("#0", text)



ventana.mainloop()