import tkinter as tk
from tkinter import scrolledtext

def run_command():
    command_output = "Your command output here"  # นำผลลัพธ์จาก Terminal มาใส่ตรงนี้
    text.insert(tk.END, command_output)
    print("hello World")

# Create the main window
root = tk.Tk()
root.title("Display Terminal Output in Tkinter")

# Create a Text widget for displaying the output
text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text.pack(pady=10)

# Create a button to run the command
button = tk.Button(root, text="Run Command", command=run_command)
button.pack(pady=10)

# Start the main event loop
root.mainloop()
