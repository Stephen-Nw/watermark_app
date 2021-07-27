from tkinter import *
from tkinter import ttk


root = Tk()
frame = ttk.Frame(root, width=500, height=500, padding=20)
frame.grid(column=0, row=0)

img_path = StringVar()
img = ttk.Entry(frame, textvariable=img_path)
img.grid(column=0, row=0, columnspan=2)

img_label = StringVar()
lbl = ttk.Label(frame, text="Upload image", padding=10)
lbl.grid(column=3, row=0)









root.mainloop()