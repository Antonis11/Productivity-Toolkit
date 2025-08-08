from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Productivity Toolkit")
window.resizable(False, False)

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


window.mainloop()