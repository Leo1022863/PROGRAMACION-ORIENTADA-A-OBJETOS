import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede agregar una tarea vacía.")

def mark_completed():
    try:
        selected_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(selected_index)
        listbox_tasks.delete(selected_index)
        listbox_tasks.insert(selected_index, f"✔ {task_text}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Crear ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")

# Campo de entrada y botón para agregar tareas
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)
entry_task.bind("<Return>", add_task)  # Permite agregar con Enter

btn_add = tk.Button(root, text="Añadir Tarea", command=add_task)
btn_add.pack()

# Lista de tareas
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

# Botones de acción
btn_complete = tk.Button(root, text="Marcar como Completada", command=mark_completed)
btn_complete.pack()

btn_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
btn_delete.pack()

# Ejecutar la aplicación
root.mainloop()
