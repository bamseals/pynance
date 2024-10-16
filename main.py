import tkinter as tk
from tkinter import ttk
import sv_ttk


# Create the main window
root = tk.Tk()
root.title("Funance")
root.geometry("900x600")


# Function to dynamically add new elements in Tab 1
def add_element_tab1():
    new_label = ttk.Label(tab1, text="New Element")
    new_label.grid(row=len(tab1.grid_slaves())//2, column=0, padx=10, pady=10, columnspan=2)

# Function to dynamically add new elements in Tab 2
def add_element_tab2():
    new_label = ttk.Label(tab2, text="Added Element in Tab 2")
    new_label.grid(row=len(tab2.grid_slaves())//2, column=0, padx=10, pady=10, columnspan=2)

# Create a notebook (tabs container)
notebook = ttk.Notebook(root)
notebook.pack(pady=0, expand=True, fill='both')  # Make it take up the entire width and height

# Create frames for the two tabs
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Add tabs to the notebook
notebook.add(tab1, text='Form 1')
notebook.add(tab2, text='Form 2')

# Form 1 elements
label1_1 = ttk.Label(tab1, text="Name:")
label1_1.grid(row=0, column=0, padx=10, pady=10)
entry1_1 = ttk.Entry(tab1)
entry1_1.grid(row=0, column=1, padx=10, pady=10)

label1_2 = ttk.Label(tab1, text="Age:")
label1_2.grid(row=1, column=0, padx=10, pady=10)
entry1_2 = ttk.Entry(tab1)
entry1_2.grid(row=1, column=1, padx=10, pady=10)

button1 = ttk.Button(tab1, text="Add Element", command=add_element_tab1)  # Add onclick event to add new elements
button1.grid(row=2, columnspan=2, pady=10)

# Form 2 elements
label2_1 = ttk.Label(tab2, text="Email:")
label2_1.grid(row=0, column=0, padx=10, pady=10)
entry2_1 = ttk.Entry(tab2)
entry2_1.grid(row=0, column=1, padx=10, pady=10)

label2_2 = ttk.Label(tab2, text="Phone:")
label2_2.grid(row=1, column=0, padx=10, pady=10)
entry2_2 = ttk.Entry(tab2)
entry2_2.grid(row=1, column=1, padx=10, pady=10)

button2 = ttk.Button(tab2, text="Add Element", command=add_element_tab2)  # Add onclick event to add new elements
button2.grid(row=2, columnspan=2, pady=10)

# Run the application
sv_ttk.set_theme("dark")
root.mainloop()
