import tkinter as tk
from tkinter import messagebox


class ToDoListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(self.master, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.master, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.mark_button = tk.Button(self.master, text="Mark as Completed", command=self.mark_as_completed)
        self.mark_button.grid(row=2, column=0, padx=10, pady=10)

        self.remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=1, padx=10, pady=10)

        self.display_button = tk.Button(self.master, text="Display Tasks", command=self.display_tasks)
        self.display_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_as_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.tasks[selected_index]["completed"] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            removed_task = self.tasks.pop(selected_index)
            messagebox.showinfo("Task Removed", f'Task "{removed_task["task"]}" removed.')
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task.")

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "No tasks in the To-Do list.")
        else:
            task_display = "\n".join(
                [f'{index + 1}. {task["task"]} - {"Completed" if task["completed"] else "Not Completed"}' for
                 index, task in enumerate(self.tasks)])
            messagebox.showinfo("To-Do List", task_display)

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            self.task_listbox.insert(tk.END, f'{task["task"]} - {status}')


def main():
    root = tk.Tk()
    todo_list_gui = ToDoListGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
