import tkinter as tk
from tkinter import messagebox
from tkinter import font

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("900x400")  

        # Initialize the tasks list
        self.tasks = []

        self.root.configure(bg="skyblue")
        self.heading_frame = tk.Frame(root, bg="black")
        self.heading_frame.pack(fill=tk.X)

        
        font_style = font.Font(size=12)

        self.task_label = tk.Label(self.heading_frame, text="Enter your task:", fg="white", bg="black", font=font_style)
        self.task_label.pack(side=tk.LEFT)

        self.task_entry = tk.Entry(self.heading_frame, font=font_style)
        self.task_entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.heading_frame, text="Add Task", command=self.add_task, font=font_style)
        self.add_button.pack(side=tk.LEFT)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=font_style)
        self.task_listbox.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, font=font_style)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, font=font_style)
        self.delete_button.pack()

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks, font=font_style)
        self.save_button.pack()

        self.load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks, font=font_style)
        self.load_button.pack()


    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_entry.get()
            if selected_task:
                self.tasks[selected_index[0]] = selected_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index[0], selected_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a task to update.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index[0])

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                self.tasks = [task.strip() for task in tasks]
                self.task_listbox.delete(0, tk.END)
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            messagebox.showerror("Error", "No saved tasks found.")

    def run(self):
        self.root.mainloop()

    
if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    todo_list.run()

