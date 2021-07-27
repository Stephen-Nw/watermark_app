from tkinter import *
from tkinter import ttk


def upload_image():
    pass


root = Tk()
root.title("Stephen Watermark App")
frame = ttk.Frame(root, width=500, height=500, padding=(20, 20, 50, 20))
frame.grid(column=0, row=0)

img_path = StringVar()
img = ttk.Entry(frame, textvariable=img_path)
img.grid(column=0, row=0, columnspan=9)

img_upload = ttk.Button(frame, text="Upload image", command=upload_image)
img_upload.grid(column=10, row=0)

root.mainloop()
