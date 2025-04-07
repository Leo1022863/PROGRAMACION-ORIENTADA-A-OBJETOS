import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas Pendientes")
        self.root.geometry("400x400")

        # Campo de entrada
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)

        # Botones
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=5)

        self.add_btn = tk.Button(self.btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(self.btn_frame, text="Marcar como Completada", command=self.mark_completed)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(self.btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Asociar teclas
        self.root.bind("<Escape>", lambda event: root.quit())
        self.root.bind("<c>", self.mark_completed)
        self.root.bind("<C>", self.mark_completed)
        self.root.bind("<d>", self.delete_task)
        self.root.bind("<D>", self.delete_task)

        # Lista de tareas y estado
        self.tasks = []
        self.completed_tasks = set()

    def add_task(self, event=None):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingrese una tarea.")

    def mark_completed(self, event=None):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.completed_tasks.add(index)
            self.update_task_list()

    def delete_task(self, event=None):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.completed_tasks = {i-1 if i > index else i for i in self.completed_tasks if i != index}
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            display_text = task
            if i in self.completed_tasks:
                display_text += " [Completada]"
            self.task_listbox.insert(tk.END, display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
