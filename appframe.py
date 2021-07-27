from tkinter import *


def upload():
    pass


def new_frame():
    root = Tk()
    root.title("Stephen Watermark app")
    root.minsize(width=500, height=300)

    frame = Frame(root, padx=100, pady=20)
    frame.grid()

    image_upload = Entry(width=21)
    image_upload.grid(row=0, column=0, columnspan=2)
    image_upload.insert(0, "placeholder information")

    upload_button = Label(frame, text="upload")
    upload_button.grid(row=0, column=4)


















    root.mainloop()
