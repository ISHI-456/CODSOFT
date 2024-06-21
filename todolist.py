#TO DO LIST APPLICATION



import tkinter as tk
from tkinter import messagebox
import time
import random
import winsound
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        reset_highlight()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        reset_highlight()
    except:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def search_task():
    search_term = search_entry.get()
    listbox.selection_clear(0, tk.END)
    reset_highlight()
    for i, task in enumerate(listbox.get(0, tk.END)):
        if search_term.lower() in task.lower():
            listbox.selection_set(i)
            listbox.itemconfig(i, {'bg':'blue', 'fg':'white'})
            return
    messagebox.showinfo("Search Result", "Task not found.")

def choose_random():
    tasks = listbox.get(0, tk.END)
    if tasks:
        random_task_index = random.randint(0, len(tasks) - 1)
        listbox.selection_clear(0, tk.END)
        reset_highlight()
        listbox.selection_set(random_task_index)
        listbox.itemconfig(random_task_index, {'bg':'blue', 'fg':'white'})
        listbox.see(random_task_index)

def start_timer():
    try:
        minutes = int(entry_time.get())
        if minutes > 0:
            seconds = minutes * 60
            remaining_label.config(text=f"Time remaining: {minutes} min")
            root.after(1000, update_timer, seconds)
        else:
            messagebox.showwarning("Warning", "Enter a valid positive time (in minutes).")
    except ValueError:
        messagebox.showwarning("Warning", "Enter a valid time (in minutes).")

def update_timer(seconds):
    if seconds > 0:
        minutes = seconds // 60
        remaining_label.config(text=f"Time remaining: {minutes} min")
        root.after(1000, update_timer, seconds - 1)
    else:
        remaining_label.config(text="Time's up!")
        play_beep_sound()

def play_beep_sound():
    winsound.Beep(1000, 5000)  
    winsound.MessageBeep(type="MB_ICONHAND")

def reset_highlight():
    for i in range(listbox.size()):
        listbox.itemconfig(i, {'bg':'white', 'fg':'black'})

def add_task_on_enter(event):
    add_task()

def search_task_on_enter(event):
    search_task


root = tk.Tk()
root.title("Enhanced To-Do List")

alarms = []

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=8)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=40)
entry.grid(row=0, column=0, padx=(0,10))

add_button = tk.Button(entry_frame, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, width=40)
search_entry.grid(row=0, column=0, padx=(0,10))

search_button = tk.Button(search_frame, text="Search Task", width=10, command=search_task)
search_button.grid(row=0, column=1)

random_button = tk.Button(root, text="Choose Random Task", width=48, command=choose_random)
random_button.pack(pady=10)

remove_button = tk.Button(root, text="Remove Selected Task", width=48, command=remove_task)
remove_button.pack()
entry.bind("<Return>", search_task_on_enter) 
entry.bind("<Return>", add_task_on_enter) 
remaining_label = tk.Label(root, text="Time remaining: ")
remaining_label.pack()
frame.pack(pady=10)

label_time = tk.Label(frame, text="Enter Time (minutes):")
label_time.pack()

entry_time = tk.Entry(frame)
entry_time.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

remaining_label = tk.Label(root, text="")
remaining_label.pack(pady=10)

root.mainloop()
