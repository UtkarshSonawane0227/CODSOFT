import tkinter as tk
from tkinter import messagebox
from tkinter import *

# add a new task
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# delete the selected task
def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to edit the selected task
def edit_task():
    try:
        index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(index)
        entry_task.delete(0, tk.END)
        entry_task.insert(tk.END, task)
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

# Create the main application window
root = tk.Tk()
root.title("To-Do List ")
root.geometry("450x600")
task_list = []

#icon apply the TO DO list frame
Image_icon = PhotoImage(file = "check-list.png")
root.iconphoto(False,Image_icon)

heading=Label(root,text="To_Do_List",width="24",fg="white",bg="#303030" ,font="Forte 25")
heading.place(x=0 ,y=0)


entry_task = tk.Entry(root, width=30,bg="white" ,font="Century 18")
entry_task.pack(pady=50)

button_add = tk.Button(root, text="Add Task", width=10, bg="#8B814C" ,command=add_task)
button_add.pack()
button_add.place(x=40,y=90)

button_delete = tk.Button(root, text="Delete Task", width=10, bg="#F08080", command=delete_task)
button_delete.pack()
button_delete.place(x=150,y=90)

button_edit = tk.Button(root, text="Edit Task", width=10, bg="#636363",command=edit_task)
button_edit.pack()
button_edit.place(x=250,y=90)

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=50)

listbox_tasks = tk.Listbox(frame_tasks, width=50 ,font="Century 15")
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

root.mainloop()
