import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la lista de eventos
        frame_lista = ttk.Frame(root)
        frame_lista.pack(pady=10)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para la entrada de datos
        frame_entradas = ttk.Frame(root)
        frame_entradas.pack(pady=10)

        # Etiquetas y campos de entrada
        ttk.Label(frame_entradas, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0)
        self.fecha_entry = ttk.Entry(frame_entradas)
        self.fecha_entry.grid(row=0, column=1)

        ttk.Label(frame_entradas, text="Hora (HH:MM):").grid(row=1, column=0)
        self.hora_entry = ttk.Entry(frame_entradas)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(frame_entradas, text="Descripción:").grid(row=2, column=0)
        self.descripcion_entry = ttk.Entry(frame_entradas)
        self.descripcion_entry.grid(row=2, column=1)

        # Frame para los botones
        frame_botones = ttk.Frame(root)
        frame_botones.pack(pady=10)

        # Botones
        ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        ttk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

        self.eventos = []

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        try:
            datetime.datetime.strptime(fecha, "%Y-%m-%d")
            datetime.datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora incorrecto.")
            return

        self.eventos.append({"fecha": fecha, "hora": hora, "descripcion": descripcion})
        self.actualizar_lista()

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showerror("Error", "Selecciona un evento para eliminar.")
            return

        item = seleccion[0]
        evento = self.eventos[self.tree.index(item)]

        if messagebox.askyesno("Confirmar", "¿Seguro que quieres eliminar este evento?"):
            self.eventos.remove(evento)
            self.tree.delete(item)

    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for evento in self.eventos:
            self.tree.insert("", tk.END, values=(evento["fecha"], evento["hora"], evento["descripcion"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()