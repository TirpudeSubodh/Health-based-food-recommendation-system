import tkinter as tk

# def print_loop():
#     result_text.delete(1.0, tk.END)  # Clear previous text
#     for i in range(1, 6):
#         result_text.insert(tk.END, f"This is iteration {i}\n")

# Create the main window
root = tk.Tk()
root.title("Loop Statement Example")


# Create a text widget to display the loop statement
result_text = tk.Text(root, height=10, width=30)
result_text.grid()
result_text.delete(1.0, tk.END)  # Clear previous text
for i in range(1, 6):
        result_text.insert(tk.END, f"This is iteration {i}\n")
# print_loop()

# Start the Tkinter event loop
root.mainloop()
