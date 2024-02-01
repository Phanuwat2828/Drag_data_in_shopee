
from main_lazada import *
from tkinter import *
from tkinter import messagebox,scrolledtext,ttk
import webbrowser
import threading
import subprocess
import sys
import shared_module 


data_link_for_lazada_gui  = {
    'อุปกรณ์-อิเล็กทรอนิกส์':0,
    'อุปกรณ์เสริม-อิเล็กทรอนิกส์':1, 
    'ทีวีและเครื่องใช้ในบ้าน':2, 
    'สุขภาพและความงาม':3, 
    'ทารกและของเล่น':4, 
    'ของชำและสัตว์เลี้ยง':5, 
    'บ้านและไลฟ์สไตล์':6, 
    'แฟชั่นและเครื่องประดับผู้หญิง':7, 
    'แฟชั่นและเครื่องประดับผู้ชาย':8,
    'กีฬาและการเดินทาง':9,
    'ยานยนต์และรถจักรยานยนต์':10
    }
class PrintRedirector:
    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.insert(END, text)
        self.textbox.see(END)
# webbrowser.open_new_tab("https://www.lazada.co.th/?spm=a2o4m.searchlistcategory.header.dhome.520251eequOvSC")
def run_system():
    global status;
    status = False
    t = threading.Thread(target=run)
    t.start();
# Create a Text widget for displaying the print statements
# Explicitly redirect stdout to the PrintRedirector
def stop_program():
    global status;
    status = True
    messagebox.showinfo("โปรแกรม'หยุดทำงาน'",f"โปรแกรม'หยุดทำงาน'");

def on_dropdown_change(event):
    selected_value = dropdown.get()
    print(f"Selected value: {selected_value}")

font1 = ("Angsana New",25)
app = Tk()


app.title("Lazda")
app.config(bg="#332941") 

app.geometry("500x900+0+0")
buttom_start = Button(app,text="start bot",bg="#9ADE7B",fg="white",command=run_system)
buttom_start.place(x=100,y=10,width=300,height=30)
buttom_stop = Button(app,text="stop bot",bg="#7360DF",fg="white",command=stop_program)
buttom_stop.place(x=100,y=50,width=300,height=30)
# entry = Entry(app, width=40)
# entry.pack(pady=10)   

# Create a Text widget for displaying the output
text = scrolledtext.ScrolledText(app, wrap=WORD, width=60, height=15)
text.pack(pady=10)
sys.stdout = PrintRedirector(text)
text.place(x=7,y=100)
# Create the main window


# Create a list of options for the dropdown
options = ['อุปกรณ์-อิเล็กทรอนิกส์', 'อุปกรณ์เสริม-อิเล็กทรอนิกส์', 'ทีวีและเครื่องใช้ในบ้าน','สุขภาพและความงาม','ทารกและของเล่น','ของชำและสัตว์เลี้ยง','บ้านและไลฟ์สไตล์','แฟชั่นและเครื่องประดับผู้หญิง','แฟชั่นและเครื่องประดับผู้ชาย','กีฬาและการเดินทาง','ยานยนต์และรถจักรยานยนต์']

# Create a StringVar to store the selected value
selected_value = StringVar()
def on_dropdown_change(event):
    selected_value = data_link_for_lazada_gui[event.widget.get()]
    shared_module.grop_number=selected_value;
    print(selected_value);

# Create the dropdown
dropdown = ttk.Combobox(app, textvariable=selected_value, values=options)
dropdown.pack(pady=10)
dropdown.place(x=10,y=360);

# Set a default value
dropdown.set(options[0])

# Bind the event handler to the <<ComboboxSelected>> event
dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)


app.mainloop()

