import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk



# Create the main window
root = tk.Tk()
root.title("Tkinter with Background Image")
bg_image= Image.open("new.png").resize((500,200))

img = ImageTk.PhotoImage(bg_image)

Label(root, image = img ).grid()

# Start the Tkinter event loop
root.mainloop()
