from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


def upload_image():
    pass


root = Tk()
root.title("Stephen Watermark App")

# =========CREATE FRAMES=====================
main_frame = ttk.Frame(root, padding=10)
upper_frame = ttk.Frame(main_frame, width=200, height=100)
lower_frame = ttk.Frame(main_frame, width=200, height=100)

# ===========CREATE OBJECTS====================
img_path = StringVar()
img = ttk.Entry(main_frame, textvariable=img_path)

img_upload = ttk.Button(main_frame, text="Upload image", command=upload_image)

my_img = ImageTk.PhotoImage(Image.open("C://Users/Stephen/Desktop/Melanin.jpg"))
my_label = Label(main_frame, image=my_img)


# ========GEOMETRY MANAGER===================
main_frame.grid(column=0, row=0)

img.grid(column=0, row=0, columnspan=4)
img_upload.grid(column=5, row=0, padx=5)

my_label.grid(column=0, row=1, columnspan=5)

# ================RESIZING=====================
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.columnconfigure(3, weight=1)
main_frame.columnconfigure(4, weight=1)
main_frame.columnconfigure(5, weight=1)

# ===========IMAGE DISPLAY==================
# my_img = ImageTk.PhotoImage(Image.open("C://Users/Stephen/Desktop/Melanin.jpg"))
# my_label = Label(upper_frame, image=my_img)
# my_label.grid(column=0, row=1, columnspan=5)

root.mainloop()
