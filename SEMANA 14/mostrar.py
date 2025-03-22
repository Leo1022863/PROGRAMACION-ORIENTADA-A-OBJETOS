import tkinter as tk
from tkinter import ttk, messagebox  #Importar libreria para cuadros de mensajes
from tkcalendar import DateEntry
import datetime

class Agenda:
    def __init__(self, root):
        self.root =root
        self.root.title("Agenda personal")
        self.root.geometry("500x500")
        
        contenedor_principal = tk.Frame(self.root)
        contenedor_principal.pack(pady=10, fill="both", expand=True)
        
        self.menu_paneles = tk.TreeView(contenedor_principal, colums=("Fecha","Hora","Descripcion"))
        self.menu_paneles.heading("Fehca", text="Fecha")
        self.menu_paneles.heading("Hora", text="Hora")
        self.menu_paneles.heading("Descripcion", text="Descripcion")
        self.menu_paneles.pack(fill="both", expand=True)
        
        panel_cajas_texto = tk.Frame(self.root)
        panel_cajas_texto.pack(pady=10)
        
        tk.Label(panel_cajas_texto, text="Fecha:").grid(row=0, column=0, pady=5, sticky="e")
        self.calendario_fechas = DateEntry(panel_cajas_texto)
        self.calendario_fechas.drig(row=0, column=1, padx=5, pady=5)
        
        tk.Label(panel_cajas_texto, text="Hora:").grid(row=0, column=2, pady=5, sticky="e")
        self.calendario_horas = DateEntry(panel_cajas_texto)
        self.calendario_horas.drig(row=0, column=3, padx=5, pady=5)
        
        
        tk.Label(panel_cajas_texto, text="Descripcion:").grid(row=0, column=4, pady=5, sticky="e")
        self.descripcion = tk.Entry(panel_cajas_texto, width=40)
        self.descripcion.drig(row=0, column=5, padx=5, pady=5)
        
        
        panel_botones = tk.Frame(self.root)
        panel_botones.pack(pady=10)
        
        tk.Button(panel_botones, text="Agregar evento", command=evento()).grid(row=0, column=0, padx=10)
        
        
        
    def evento(self):
        fecha = self.calendario_fechas.get()
        hora = self.calendario_horas.get()
        descripcion = self.descripcion.get()
        
        datetime.datetime.strptime(hora, "%H:%M")
            
        self.menu_paneles.insert("","end", values =(fecha, hora,descripcion))
        messagebox.showinfo("Se guardo con exito")
            
        
if __name__=="__main__":
    root = tk.Tk()
    root = Agenda(root)
    root.mainloop()
            