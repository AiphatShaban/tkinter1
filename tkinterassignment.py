import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Subtraction Program")

Label = ttk.Label(window,text="Enter two numbers and click the 'minus' button")
Label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

num1_entry = ttk.Entry(window)
num2_entry = ttk.Entry(window)

num1_entry.grid(row=1, column=0, padx=10, pady=5)
num2_entry.grid(row=1, column=1, padx=10, pady=5)

def subtract_numbers():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 - num2
        result_Label.config(text=f"Result: {result}")
    except ValueError:
        result_Label.config(text="Invalid input")

minus_button = ttk.Button(window, text="minus", command=subtract_numbers)
minus_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the result
result_Label = ttk.Label(window, text="Result: ")
result_Label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter main loop
window.mainloop()
