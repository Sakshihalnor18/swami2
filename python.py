import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.display_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.tasks.remove(selected_task)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def display_tasks(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if _name_ == "_main_":
    main()
