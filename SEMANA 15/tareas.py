import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class aplicacion_tareas:
    def __init__(self, root):
        self.root =root #cargando el atributo de la clase
        
        self.root.title("Gestor de tareas")
        self.geometry("400x500")
        
        self.tareas = [] # lista para guardar las tareas
        
        #DISEÑO DE LA VENTANA
        self.frame_principal = ttk.Frame(self.root, padding="10")
        self.frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        #CAJAS DE TEXTO
        self.entrada_tarea = ttk.Entry(self.frame_principal, width=40)
        self.entrada_tarea.grid(row=0, column=0, columnspan=2, pady=5)
        self.entrada_tarea.bind('<Return>', self.crear_tarea)
        
        #BOTON PARA CREAR LA TAREA
        self.btn_crear_tarea = ttk.Button(self.frame_principal, "Crear tarea", command=self.btn_crear_tarea)
        self.btn_crear_tarea.grid(row=0, column=2, padx= 5, pady=5)
        
        self.lista = tk.Listbox(self.frame_principal, width=50, height=20)
        self.lista.grid(row=1, column=0, columnspan=3, pady=10)
        self.lista.bind('<Double-Button-1>', self.marca_completada)
        
        self.frame_botones = ttk.Button(self.frame_principal)
        self.frame_botones.grid(row=2, column=0, columnspan=3, pady=5)
        
        self.boton_completado = ttk.Button(self.frame_botones, text="Marcar como completada",
        command=lambda: self.marca_completada(None))
        self.boton_completado.pack(side=tk.LEFT, padx=5)
        
        self.eliminar = ttk.Button(self.frame_botones, text="Eliminar", command=self.eliminar_tarea)
        self.eliminar.pack(side=tk.LEFT, padx=5)
        
    def crear_tarea(self, event=None):
        tarea = self.entrada_tarea.get().strip()
        if tarea:
            self.tareas.append({"texto":tarea, "Completada":False})
            for tar in self.tareas:
                texto = tar["texto"]
                if tar["Completada"]:
                    texto = "x" + texto
            self.lista.insert(tk.END, texto)
            
        
        
        
        
root = tk.Tk()
app = aplicacion_tareas(root)
root.mainloop()
        
        