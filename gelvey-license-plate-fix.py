import os
import fileinput
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def search_and_delete_license(parent_directory):
    for root, dirs, files in os.walk(parent_directory):
        for file in files:
            if file.endswith(".pc"):
                file_path = os.path.join(root, file)

                with fileinput.FileInput(file_path, inplace=True) as f:
                    for line in f:
                        if "licenseName" not in line:
                            print(line, end='')

def browse_button():
    filename = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, filename)

def process_files():
    parent_directory = entry_path.get()
    if os.path.isdir(parent_directory):
        search_and_delete_license(parent_directory)
        result_label.config(text="Process completed successfully.")
    else:
        result_label.config(text="Invalid directory path.")

# Create main window
root = tk.Tk()
root.title("Gelvey-LPF License Plate Deletion App")

# Configure styles for a more customized appearance
style = ttk.Style()

# Set the theme to 'clam' (tkinter default theme) for Entry widget
style.theme_use("clam")

# Set the background and foreground colors for Entry widget
style.configure("TEntry",
                fieldbackground="#FFD700",  # Orange
                foreground="black")

# Set the background and foreground colors for Button widgets
style.configure("TButton",
                background="#FFD700",  # Orange
                foreground="black")

# Create and place widgets
label_path = tk.Label(root, text="Select Parent Directory:")
label_path.pack(pady=10)

entry_path = ttk.Entry(root, width=40)
entry_path.pack(pady=10)

button_browse = ttk.Button(root, text="Browse", command=browse_button)
button_browse.pack(pady=10)

button_process = ttk.Button(root, text="Process Files", command=process_files)
button_process.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()