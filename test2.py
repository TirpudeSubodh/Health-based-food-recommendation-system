import tkinter as tk
from tkinter import ttk

def change_color():
    # Change the background color of the combobox
    combo_style.configure('TCombobox', fieldbackground=color_var.get())

# Create the main window
root = tk.Tk()
root.title("Tkinter Combobox Color Change")

# Create a Combobox style
combo_style = ttk.Style()
combo_style.configure('TCombobox', padding=(5, 5, 5, 5))

# Create a Combobox
combo_values = ["Option 1", "Option 2", "Option 3"]
combo_var = tk.StringVar()
combo = ttk.Combobox(root, textvariable=combo_var, values=combo_values)
combo.pack(padx=10, pady=10)

# Create a Label and Entry for color input
color_label = tk.Label(root, text="Enter Color:")
color_label.pack(pady=5)
color_var = tk.StringVar(value='#ffffff')  # Default color is white
color_entry = tk.Entry(root, textvariable=color_var)
color_entry.pack(pady=5)

# Create a Button to change the color
change_color_button = tk.Button(root, text="Change Color", command=change_color)
change_color_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
