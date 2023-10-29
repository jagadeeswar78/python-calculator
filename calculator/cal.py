import tkinter as tk
from tkinter import font

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for input/output with a larger font and width
entry_font = font.Font(family="Arial", size=20)
entry = tk.Entry(root, font=entry_font, width=15, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons with larger dimensions
button_font = font.Font(family="Arial", size=16)
buttons = [
    'C',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
   
]

# Create and display buttons
row_num = 1
col_num = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=button_font, command=calculate).grid(row=row_num, column=col_num)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=button_font, command=clear).grid(row=row_num, column=col_num)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=button_font, command=lambda b=button: button_click(b)).grid(row=row_num, column=col_num)

    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Increase window size
root.geometry("400x500")

# Run the application
root.mainloop()