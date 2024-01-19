#Jalanin pake python 3 ya, soalnya ada ada syntax yang ga ada di python 2

import tkinter as tk
from tkinter import messagebox

#Ini Abstract Class dan Interface
class AbstractTask:
    #Ini Constructor
    def __init__(self, title, description, label):
        self.title = title
        self.description = description
        self.label = label

    def perform_task(self):
        pass

#Ini Inheritence dan Polymorphism pake Overiding
class Task(AbstractTask):
    def perform_task(self):
        print(f"Performing task: {self.title} - {self.description} - {self.label}")


#Ini Encapsulation
class ToDoList:
    #Ini Constructor
    def __init__(self):
        #Ini ArrayList
        self.__tasks = []

    #Ini mirip overloading, karena bisa menerima Task dengan 3 parameter. Soalnya python ga ada overloading
    def add_task(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], Task):
            task = args[0]
        elif len(args) == 3:
            task = Task(*args)
        else:
            raise ValueError("Invalid arguments for adding task")
        
        self.__tasks.append(task) 

    def get_tasks(self):
        return self.__tasks

#Ini Inheritence kaena turunan dari Entry
class PlaceholderEntry(tk.Entry):
    #Ini Constructor
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', width=None):
        super().__init__(master, width=width)

        self.placeholder = placeholder
        self.placeholder_color = color #Ini Encapsulation(?)
        self.default_fg_color = self['fg'] #Ini juga Encapsulation(?)

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    #Ini Polymorphism
    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    #Ini Polymorphism juga
    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

#Ini GUI
class ToDoListGUI:
    #Ini Constructor
    def __init__(self, root, todolist):
        self.todolist = todolist
        self.root = root
        self.root.title("To-Do List")

        self.title_entry = PlaceholderEntry(root, "Judul", 'grey', width=100)
        self.title_entry.pack()

        self.description_entry = PlaceholderEntry(root, "Deskripsi", 'grey', width=100)
        self.description_entry.pack()

        self.label_entry = PlaceholderEntry(root, "Label", 'grey', width=100)
        self.label_entry.pack()

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.pack()

        self.update_tasks_display()

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        label = self.label_entry.get()

        if not title or not description or not label:
            messagebox.showwarning("Warning", "Semua field harus diisi")
            return

        #Ini Exception Handling
        try:
            task = Task(title, description, label)
            self.todolist.add_task(task)
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.label_entry.delete(0, tk.END)
            self.update_tasks_display()
        except Exception as e:  # Exception Handling
            messagebox.showerror("Error", str(e))

    def update_tasks_display(self):
        #Ini Encapsulation, karne tasks_frame adalah private
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        #Ini Polymorphism dan juga ada konsep Collection, karena get_tasks() bisa mengembalikan list dari Task dan menampilkan kumpulan tasknya
        for task in self.todolist.get_tasks():
            #Ini input outputnya
            task_text = f"{task.title} - {task.description} [{task.label}]"
            task_label = tk.Label(self.tasks_frame, text=task_text)
            task_label.pack()

if __name__ == "__main__":
    todolist = ToDoList()
    root = tk.Tk()
    gui = ToDoListGUI(root, todolist)
    root.mainloop()