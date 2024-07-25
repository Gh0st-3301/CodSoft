import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Task input
        self.task_input = tk.Entry(root, width=40)
        self.task_input.grid(row=0, column=0, padx=10, pady=10)

        # Add task button
        tk.Button(root, text="Add Task", command=self.add_task).grid(row=0, column=1, padx=10, pady=10)

        # Task list
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Delete task button
        tk.Button(root, text="Delete Task", command=self.delete_task).grid(row=2, column=0, padx=10, pady=10)

        # Mark as complete button
        tk.Button(root, text="Mark as Complete", command=self.mark_as_complete).grid(row=2, column=1, padx=10, pady=10)

        # Clear all tasks button
        tk.Button(root, text="Clear All", command=self.clear_tasks).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_listbox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            del self.tasks[task_index]
            self.task_listbox.delete(task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_as_complete(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.tasks[task_index]["completed"] = True
            self.task_listbox.itemconfig(task_index, )  
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")
            
    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks.clear()

def main():
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
