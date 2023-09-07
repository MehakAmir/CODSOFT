import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To Do List")

heading=tk.Label(root,text="Please Enter Task",font="arial 20 bold",fg="black")
heading.place(x=60,y=15)
heading.pack(pady=3)

entry = tk.Entry(root, width=40, bg="#FCE8E8",fg="black",font="arial 18 bold")
entry.pack(pady=50)

add_button = tk.Button(root, text="Add Task",font="arial 15 bold",fg="white",bg="green", command=add_task)
add_button.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", font="arial 15 bold",fg="white",bg="orange",command=remove_task)
remove_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear All Tasks", font="arial 15 bold",fg="white",bg="red", command=clear_tasks)
clear_button.pack(pady=10)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, fg="black",bg="#FCE8E8",font="arial 18 bold")
listbox.pack(pady=10)

root.mainloop()








