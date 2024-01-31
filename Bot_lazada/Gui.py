
from main_lazada import *
from tkinter import *
from tkinter import messagebox,font
import webbrowser
import threading

# webbrowser.open_new_tab("https://www.lazada.co.th/?spm=a2o4m.searchlistcategory.header.dhome.520251eequOvSC")
def run_system():
    global status;
    status = False
    t = threading.Thread(target=run)
    t.start()
def stop_program():
    global status;
    status = True
    messagebox.showinfo("โปรแกรม'หยุดทำงาน'",f"โปรแกรม'หยุดทำงาน'");


def updatetitle():
    count = int(title.get().split(' ')[-1])+1
    title.set(f"count Excel {count}")


font1 = ("Angsana New",25)
Font = font.Font(family="league Spartan")
app = Tk()
app.title("Lazda")
app.config(bg="#332941",font=font) 

app.geometry("500x500+0+0")
buttom_start = Button(app,text="start bot",bg="#9ADE7B",fg="white",command=run_system)
buttom_start.place(x=100,y=10,width=300,height=30)
buttom_stop = Button(app,text="stop bot",bg="#7360DF",fg="white",command=stop_program)
buttom_stop.place(x=100,y=50,width=300,height=30)
title = StringVar()
title.set(f"count Excel 0")
title_show = Label(app,textvariable=title)
title_show.place(x=100,y=200,width=300,height=20)
app.mainloop()






