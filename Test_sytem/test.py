import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x200')
root.tk_setPalette(background='#ececec')
root.option_add('*Font', 'Arial 12')

font_thai = ('Arial', 12)

options = [
    'อุปกรณ์-อิเล็กทรอนิกส์', 'อุปกรณ์เสริม-อิเล็กทรอนิกส์', 'ทีวีและเครื่องใช้ในบ้าน',
    'สุขภาพและความงาม', 'ทารกและของเล่น', 'ของชำและสัตว์เลี้ยง', 'บ้านและไลฟ์สไตล์',
    'แฟชั่นและเครื่องประดับผู้หญิง', 'แฟชั่นและเครื่องประดับผู้ชาย', 'กีฬาและการเดินทาง',
    'ยานยนต์และรถจักรยานยนต์'
]

# สร้างดิกชันนารีเพื่อเก็บค่าตัวเลขที่เกี่ยวข้องกับแต่ละตัวเลือก
selected_values = {
    'อุปกรณ์-อิเล็กทรอนิกส์': 0,
    'อุปกรณ์เสริม-อิเล็กทรอนิกส์': 1,
    'ทีวีและเครื่องใช้ในบ้าน': 2,
    'สุขภาพและความงาม': 3,
    'ทารกและของเล่น': 4,
    'ของชำและสัตว์เลี้ยง': 5,
    'บ้านและไลฟ์สไตล์': 6,
    'แฟชั่นและเครื่องประดับผู้หญิง': 7,
    'แฟชั่นและเครื่องประดับผู้ชาย': 8,
    'กีฬาและการเดินทาง': 9,
    'ยานยนต์และรถจักรยานยนต์': 10
}

selected_value_var = tk.StringVar()

def on_dropdown_change(event):
    selected_value = selected_values[event.widget.get()]
    selected_value_var.set(selected_value)
    # print(f"Selected value for {event.widget.get()}: {selected_value}")

root.title("Dropdown in Tkinter")

dropdown = ttk.Combobox(root, textvariable=selected_value_var, values=options, font=font_thai)
dropdown.pack(pady=10)

dropdown.set(options[0])

dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)

root.mainloop()

