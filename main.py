from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


def upload_image():
    pass


root = Tk()
root.title("Stephen Watermark App")
main_frame = ttk.Frame(root, padding=10)

# ===========CREATE OBJECTS====================
image_address = StringVar()
original_image = ttk.Entry(main_frame, textvariable=image_address, width=75, justify="right")

upload_button = ttk.Button(main_frame, text="Upload image", command=upload_image)

watermarked_image = ImageTk.PhotoImage(Image.open("C://Users/Stephen/Desktop/Melanin.jpg"))
my_label = Label(main_frame, image=watermarked_image)


# ========GEOMETRY MANAGER===================
main_frame.grid(column=0, row=0)
original_image.grid(column=0, row=0)
upload_button.grid(column=2, row=0)
my_label.grid(column=0, row=1, columnspan=3)


# ================RESIZING=====================
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.columnconfigure(3, weight=1)


root.mainloop()
