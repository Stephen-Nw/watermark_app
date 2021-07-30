from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Stephen Watermark App")
main_frame = ttk.Frame(root, padding=10)


def upload_image():
    image_path = image_entry.get()
    watermarked_image = ImageTk.PhotoImage(Image.open(image_path))
    image_display = Label(main_frame, image=watermarked_image)
    image_display.image_names = watermarked_image
    image_display.grid(column=0, row=1, columnspan=3)
    return


# ===========CREATE OBJECTS====================
image_address = StringVar()
image_entry = ttk.Entry(main_frame, textvariable=image_address, width=75, justify="right")
upload_button = ttk.Button(main_frame, text="Upload image", command=upload_image)


# ========GEOMETRY MANAGER===================
main_frame.grid(column=0, row=0)
image_entry.grid(column=0, row=0)
upload_button.grid(column=2, row=0)


# ================RESIZING=====================
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.columnconfigure(3, weight=1)


root.mainloop()
