from tkinter import *
from tkinter import ttk
from tkinter import filedialog

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


window.mainloop()