import tkinter as tk
import pyautogui

def show_position():
    x, y = pyautogui.position()
    position_label.config(text=f"Mouse Position: x={x}, y={y}")

# Create the main window
root = tk.Tk()
root.title("Mouse Position Viewer")

# Create a label to display the mouse position
position_label = tk.Label(root, text="Mouse Position: ")
position_label.pack(pady=10)

# Create a button to trigger the display of the mouse position
show_position_button = tk.Button(root, text="Show Position", command=show_position)
show_position_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()