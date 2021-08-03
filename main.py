from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Stephen Watermark App")
main_frame = ttk.Frame(root, padding=10)


# def upload_image():
#     """Receives image for processing; throws error for invalid entries"""
#     image_path = image_entry.get()
#     global watermarked_image
#     try:
#         watermarked_image = ImageTk.PhotoImage(Image.open(image_path))
#     except AttributeError:
#         messagebox.showerror(title="Error!!", message="Image path is not valid!")
#     except FileNotFoundError:
#         messagebox.showerror(title="Error!!", message="No File Found!")
#     else:
#         image_display = Label(main_frame, image=watermarked_image)
#         # image_display.image_names = watermarked_image  # needed for PhotoImage to work inside a function; not sure why
#         image_display.grid(column=0, row=1, columnspan=3)


def upload_image():
    """Receives image for processing; throws error for invalid entries"""
    image_path = image_entry.get()
    global watermarked_image
    try:
        watermarked_image = ImageTk.PhotoImage(Image.open(image_path))
    except AttributeError:
        messagebox.showerror(title="Error!!", message="Image path is not valid!")
    except FileNotFoundError:
        messagebox.showerror(title="Error!!", message="No File Found!")
    else:
        canvas = Canvas(main_frame, background='red', width=550, height=550)
        # image_display = Label(canvas, image=watermarked_image)
        canvas.grid(column=0, row=1, columnspan=3)
        # image_display.grid(column=0, row=1, columnspan=3)
        canvas.create_image(10, 10, image=watermarked_image, anchor="nw")
        canvas.create_text(100, 500, text="welcome", font=('Helvetica', 25, "bold"), fill='white')




def enter(event):
    """Receives image for processing; throws error for invalid entries"""
    image_path = image_entry.get()
    global watermarked_image
    try:
        watermarked_image = ImageTk.PhotoImage(Image.open(image_path))
    except AttributeError:
        messagebox.showerror(title="Error!!", message="Image path is not valid!")
    except FileNotFoundError:
        messagebox.showerror(title="Error!!", message="No File Found!")
    else:
        image_display = Label(main_frame, image=watermarked_image)
        # image_display.image_names = watermarked_image  # needed for PhotoImage to work inside a function; not sure why
        image_display.grid(column=0, row=1, columnspan=3)
    return

# ===========CREATE OBJECTS====================
image_address = StringVar()
image_entry = ttk.Entry(main_frame, textvariable=image_address, width=75, justify="right")
upload_button = ttk.Button(main_frame, text="Upload image", command=upload_image)
image_entry.bind(sequence='<Key-Return>', func=enter)

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

# TODO 3: Create and add watermark to picture
# TODO 4: Refactor code - functional programming


root.mainloop()
