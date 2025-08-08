from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import font

window = Tk()
window.title("Productivity Toolkit")
window.resizable(False, False)

def on_tab_change(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

    if tab_text == "Notebook":
        window.config(menu=menubar)
    else:
        window.config(menu="")

notebook = ttk.Notebook(window)

notes = Frame(notebook)
to_do_list = Frame(notebook)
settings = Frame(notebook)
painting = Frame(notebook)
about = Frame(notebook)

notebook.add(notes, text="Notebook")
notebook.add(to_do_list, text="To Do List")
notebook.add(settings, text="Settings")    
notebook.add(painting, text="Painting")
notebook.add(about, text="About")

notebook.pack(expand=True, fill=BOTH) 

notebook.bind("<<NotebookTabChanged>>", on_tab_change)

# Tab Notebook

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Documents",
                                            title="Open File",
                                            filetypes=(("text files","*.txt"), ("all files", ".*")))
    file = open(filepath,"r")
    text.insert(1.0, file.read())
    file.close()

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Documents",
                                    defaultextension='.txt',
                                    filetypes=[("Text File", ".txt"), ("All files", ".*")])
    
    if file is None:
        return
    
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    text.delete(1.0, END)
    file.close()

def newFile():
    text.delete(1.0, END)

text = Text(notes, bg="light yellow", font=("Ink Free", 20), height=10, width=30, padx=10, pady=10, fg="green") 
text.pack()

menubar = Menu(window)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 10))
menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_cascade(label="Open", command=openFile)
fileMenu.add_cascade(label="Save", command=saveFile)
fileMenu.add_cascade(label="New", command=newFile)

# Tab To Do List

def add():
    global index
    listbox.insert(index,entry.get())
    index += 1
    entry.delete(0, END)

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

def complete():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        old_text = listbox.get(index)
        new_text = old_text + " ✅"
        listbox.delete(index)
        listbox.insert(index, new_text)

index = 1

entry = Entry(to_do_list, font=('Arial',20))
entry.place(relx=0.01, rely=0.07, anchor="w")

add_button = Button(to_do_list, width=5, text="Add", command=add)
add_button.place(relx=0.77, rely=0.07, anchor="e")

listbox = Listbox(to_do_list, height=10, width=60)
listbox.place(relx=0.01, rely=0.5, anchor="w")

delete_button = Button(to_do_list, width=5, text="Delete", command=delete)
delete_button.place(relx=0.32, rely=0.8, anchor="center")

complete_task_button = Button(to_do_list, width=8, text="Complete", command=complete)
complete_task_button.place(relx=0.44, rely=0.8, anchor="center")

# Tab Settings

def change_fg_color_notes():
    color = colorchooser.askcolor(title="Choose Text Color")
    colorHex = color[1]
    text.config(fg=colorHex)
    fg_color_preview.config(bg=colorHex)

def change_bg_color_notes():
    color = colorchooser.askcolor(title="Choose Background Color")
    colorHex = color[1]
    text.config(bg=colorHex)
    bg_color_preview.config(bg=colorHex)

frame = Frame(settings)
frame.place(x=0,y=0)

notes_tab = Label(frame, text="Notebook:", font=font.Font(underline=1, family="Arial", size=14))
notes_tab.grid(row=0, column=0, padx=5, columnspan=2)

foreground_notes = Label(frame, text="Text Color:")
foreground_notes.grid(row=1, column=0)

fg_color_preview = Label(frame, width=3, bg="green", relief="solid")
fg_color_preview.grid(row=1, column=1, pady=5)
fg_color_preview.bind("<Button-1>", lambda e: change_fg_color_notes())

background_notes = Label(frame, text="Background Color:")
background_notes.grid(row=2,column=0)

bg_color_preview = Label(frame, width=3, bg="light yellow", relief="solid")
bg_color_preview.grid(row=2, column=1)
bg_color_preview.bind("<Button-1>", lambda e: change_bg_color_notes())

def set_light_mode():
    to_do_list.config(bg="SystemButtonFace")
    entry.config(bg="SystemWindow", fg="SystemWindowText")
    listbox.config(bg="SystemWindow", fg="SystemWindowText")
    add_button.config(bg="SystemButtonFace", fg="SystemButtonText")
    delete_button.config(bg="SystemButtonFace", fg="SystemButtonText")
    complete_task_button.config(bg="SystemButtonFace", fg="SystemButtonText")

def set_dart_mode():
    to_do_list.config(bg="#2E2E2E")
    text.config(bg="#1E1E1E", fg="white", insertbackground="white")
    add_button.config(bg="#3C3F41", fg="white")
    delete_button.config(bg="#3C3F41", fg="white")
    complete_task_button.config(bg="#3C3F41", fg="white")

options = ["light","dark"]

def choose_mode():
    if(x.get() == 0):
        set_light_mode()
    elif(x.get() == 1):
        set_dart_mode()

x = IntVar()

to_do_list_tab = Label(frame, text="To Do List:", font=font.Font(underline=1, family="Arial", size=14))
to_do_list_tab.grid(row=3, column=0, padx=5, columnspan=2)

mode_to_do_list = Label(frame, text="Mode:")
mode_to_do_list.grid(row=4, column=0)

for index in range(len(options)):
    radiob = Radiobutton(frame, text=options[index], value=index, variable=x, command=choose_mode)

    radiob.grid(row=4, column=index+1)

# Tab Painting

def old_point(event):
    global old_x, old_y
    old_x, old_y = event.x, event.y

def new_point(event):
    global old_x, old_y
    new_x, new_y = event.x, event.y

    canvas.create_line(old_x, old_y, new_x, new_y, fill=current_color, width=2)

    old_x, old_y = new_x, new_y
    
def change_color():
    global current_color
    color = colorchooser.askcolor(title="Choose Color")
    colorHex = color[1]
    current_color=colorHex
    color_label.config(bg=colorHex)

def clear():
    canvas.delete("all")

current_color = "black"

canvas = Canvas(painting)
canvas.pack()

canvas.bind("<Button-1>", old_point)
canvas.bind("<B1-Motion>", new_point)

color_label = Label(painting, width=3, bg=current_color, relief="solid")
color_label.place(relx=0.42, rely=0.94)
color_label.bind("<Button-1>", lambda e: change_color())

clear_button = Button(painting, text="Clear", width=5, command=clear)
clear_button.place(relx=0.49, rely=0.93)


window.mainloop()