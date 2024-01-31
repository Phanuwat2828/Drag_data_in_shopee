
from main_shopee import *
from tkinter import *
import webbrowser

webbrowser.open_new_tab("https://goole.com")

def updatetitle():
    count = int(title.get().split(' ')[-1])+1
    title.set(f"count Excel {count}")

font1 = ("Angsana New",25)
app = Tk()
app.title("bot shopee")
app.geometry("500x500+0+0")
buttom_start = Button(app,text="start bot",bg="gold",command=run)
buttom_start.place(x=100,y=10,width=300,height=30)
title = StringVar()
title.set(f"count Excel 0")
title_show = Label(app,textvariable=title)
title_show.place(x=100,y=100,width=300,height=20)
app.mainloop()






