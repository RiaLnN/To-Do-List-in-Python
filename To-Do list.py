import tkinter
import tkinter.messagebox
import pickle



tasks_status = []

def add_ex ():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        tasks_status.append(False)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title = "WARNING", message="Enter a task")

def load_ex ():
    global tasks_status
    try:
        tasks_data = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        tasks_status = []
        for task_text, done in tasks_data:
            listbox_tasks.insert(tkinter.END, format_task(task_text, done))
            tasks_status.append(done)
    except:
        tkinter.messagebox.showwarning(title="WARNING", message="Nothing to load")

def del_ex():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
        tasks_status.pop(task_index)
    except:
        tkinter.messagebox.showwarning(title="WARNING", message="Select a task")

def save_ex():
    tasks_data = []
    for i in range(listbox_tasks.size()):
        task_text = listbox_tasks.get(i)
        clean_text = task_text.replace("✔ ", "").replace("~~", "")
        done = tasks_status[i]
        tasks_data.append((clean_text, done))
    pickle.dump(tasks_data, open("tasks.dat", "wb"))

def check_ex():
    try:
        task_index = listbox_tasks.curselection()[0]
        tasks_status[task_index] = not tasks_status[task_index]
        task_text = listbox_tasks.get(task_index)
        clean_text = task_text.replace("✔ ", "").replace("~~", "")
        listbox_tasks.delete(task_index)
        listbox_tasks.insert(task_index, format_task(clean_text, tasks_status[task_index]))
    except:
        tkinter.messagebox.showwarning(title="WARNING", message="Select a task")

def format_task(text, done):
    if done:
        return f"✔ ~~{text}~~"
    else:
        return text

root = tkinter.Tk()
root.title("To-Do List")

frame_task = tkinter.Frame(root)
frame_task.pack()

listbox_tasks = tkinter.Listbox(frame_task, height = 15, width=55)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_task = tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_tasks.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=55)
entry_task.pack()
button_add = tkinter.Button(root, text = "Add task", width = 50, command= lambda: add_ex())
button_add.pack()

button_delete = tkinter.Button(root, text = "Delete task", width = 50, command= lambda: del_ex())
button_delete.pack()

button_check = tkinter.Button(root, text="Mark as done / undone", width=50, command=check_ex)
button_check.pack()

button_load = tkinter.Button(root, text = "Load task", width = 50, command= lambda: load_ex())
button_load.pack()

button_save = tkinter.Button(root, text = "Save task", width = 50, command= lambda: save_ex())
button_save.pack()
root.mainloop()