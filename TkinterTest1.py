from Tkinter import *

root = Tk()

#w = Label(root, text="Hello World!")
#w.pack()

w1 = Label(root).pack(side="right")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""
w2 = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=explanation).pack(side="left")
root.mainloop()
