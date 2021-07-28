from tkinter import *
from tkinter import ttk


def upload_image():
    pass


root = Tk()
root.title("Stephen Watermark App")

# =========CREATE FRAMES=====================
main_frame = ttk.Frame(root, padding=10)
upper_frame = ttk.Frame(main_frame,  width=200, height=100)
lower_frame = ttk.Frame(main_frame,  width=200, height=100)


# ===========CREATE OBJECTS====================
img_path = StringVar()
img = ttk.Entry(upper_frame, textvariable=img_path)

img_upload = ttk.Button(upper_frame, text="Upload image", command=upload_image)


# ========GEOMETRY MANAGER===================
main_frame.grid(column=0, row=0)
upper_frame.grid(column=0, row=0, columnspan=5)
lower_frame.grid(column=0, row=1, columnspan=5, rowspan=5)

img.grid(column=0, row=0, columnspan=4)
img_upload.grid(column=5, row=0, padx=5)


# ================RESIZING=====================
# main_frame.columnconfigure(0, weight=1)
# main_frame.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
upper_frame.columnconfigure(0, weight=1)
upper_frame.columnconfigure(1, weight=1)
upper_frame.columnconfigure(2, weight=1)
upper_frame.columnconfigure(3, weight=1)
upper_frame.columnconfigure(4, weight=1)
upper_frame.columnconfigure(5, weight=1)



root.mainloop()

