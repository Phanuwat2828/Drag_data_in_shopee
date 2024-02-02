import tkinter as tk
from tkinter import scrolledtext
import subprocess
import os

path_file = os.getcwd()+r'\Bot_lazada\main_lazada.py'
def run_code():
    global process
    code_path = path_file
    try:
        process = subprocess.check_output(["python", code_path], stderr=subprocess.STDOUT, text=True)
        output_text.insert(tk.END, f"Output:\n{process.stdout.read()}\n\n")
    except subprocess.CalledProcessError as e:
        output_text.insert(tk.END, f"Error:\n{e.output}\n\n")
def stop_code():
    if 'process' in globals() and process.poll() is None:
        process.terminate()
        output_text.insert(tk.END, "Code execution terminated.\n\n")
    else:
        output_text.insert(tk.END, "No running code to stop.\n\n")
# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("Lazada And Shopee")

# ปุ่มรันโค้ด
run_button = tk.Button(root, text="Run",width=10,height=2, command=run_code)
run_button.pack(side=tk.RIGHT,padx=10)
# Stop
stop_button = tk.Button(root, text="Stop Code",width=10,height=2, command=stop_code)
stop_button.pack(side=tk.RIGHT, padx=10)

# TextArea สำหรับแสดงผลลัพธ์
output_text = scrolledtext.ScrolledText(root, width=60, height=50)
output_text.pack(padx=10, pady=10)

# รัน GUI
root.mainloop()


                            