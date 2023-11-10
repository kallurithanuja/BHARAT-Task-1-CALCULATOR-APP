import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()

    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widget for display
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 14), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons and add them to the grid
row_val = 1
col_val = 0
for button_text in buttons:
    tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 12),
              command=lambda b=button_text: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI application
root.mainloop()
