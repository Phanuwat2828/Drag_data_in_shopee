# ++++++++++++++++++++++++++++++ gui ++++++++++++++++++++ import 
from tkinter import *
from tkinter import messagebox,scrolledtext,ttk
import webbrowser
import threading
import subprocess
import sys
# ++++++++++++++++++++++++++++++ gui ++++++++++++++++++++

# ++++++++++++++++++++++++++++++ main ++++++++++++++++++++ import 
import requests,os,json,time,pandas as pd,pyautogui,shutil,pyperclip,keyboard as ky
from fnmatch import fnmatch
from pynput import keyboard,mouse
from data_address import address as ad
# ++++++++++++++++++++++++++++++ main ++++++++++++++++++++

# ============================== variable ================= main
class ReadAndWriteLog():
    def __init__(self):
        self.df = []
        self.datas = []
    def addLog(self,data):
        try:
            open('./log/log.txt',mode='a',encoding='utf-8').write(data+'\n')
        except:
            open('./log/log.txt',mode='w',encoding='utf-8').write(data+'\n')
    def getLog(self):
        self.datas = []
        self.df = open('./log/log.txt',mode='r',encoding='utf-8').readlines()
        for i in self.df:
            self.datas.append(i[:-1])
        return self.datas
    def clearLog(self):
        open('./log/log.txt',mode='w',encoding='utf-8').write('')
        setTreeCommand()
class PrintRedirector:
    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.insert(END, text)
        self.textbox.see(END)

# path_api
uri_API = 'https://8f34-14-207-201-178.ngrok-free.app/';
# path
bot_shopee = r'\Bot_shopee';
path_file = os.getcwd();
drag_data = os.path.abspath(os.path.join(path_file, os.pardir))
data_shopee = r'\Data_shopee';
data_shopee_xlsx = r'\shopee.xlsx';
un_process = r'\Unprocess';
data_link = r'\Data_link\data_link_all.json';
desk_top = 8;
# head_excel
header_2 = ['col-xs-2-4 href', 'Fd4QmV src', 'FTxtVW',
       'customized-overlay-image src', 'DgXDzJ', 'bPcAVl', 'k9JZlv',
       'bx++ig 2', 'k9JZlv 2', 'OwmBnn', 'JVW3E2', 'hxLzax']
header_Values = {
    'col-xs-2-4 href':"product",
    'Fd4QmV src':"image_product_1",
    'FTxtVW':"discount",
    'customized-overlay-image src':"image_product_2",
    'DgXDzJ':"data_product", 
    'bPcAVl':"price_before",
    'k9JZlv':"price_product_1",
    'bx++ig 2':"Emoji",
    'k9JZlv 2':"price_product_2",
    'OwmBnn':"sold",
    'JVW3E2':"place", 
    'hxLzax':"Recommended_shops"
}
# Link_all
data_link_for_shopee  = {
    0: 'อุปกรณ์-อิเล็กทรอนิกส์',
    1: 'อุปกรณ์เสริม-อิเล็กทรอนิกส์', 
    2: 'ทีวีและเครื่องใช้ในบ้าน', 
    3: 'สุขภาพและความงาม', 
    4: 'ทารกและของเล่น', 
    5: 'ของชำและสัตว์เลี้ยง', 
    6: 'บ้านและไลฟ์สไตล์', 
    7: 'แฟชั่นและเครื่องประดับผู้หญิง',
    8: 'แฟชั่นและเครื่องประดับผู้ชาย',
    9: 'กีฬาและการเดินทาง',
    10: 'ยานยนต์และรถจักรยานยนต์',
    11:"เครื่องประดับ",
    12:"ตั๋วและบัตรกำนัน"}
# ============================== variable =================
# ============================== variable ================= gui
font1 = ("Angsana New",25)
app = Tk()
app.title("Shopee")
app.config(bg="#332941") 
app.geometry("500x900+0+0")

selected_value = StringVar()
showStatusBot = StringVar()
log = ReadAndWriteLog()
data_link_for_shopee_gui  = {
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
    'ยานยนต์และรถจักรยานยนต์':10,
    "เครื่องประดับ":11,
    "ตั๋วและบัตรกำนัน":12
}
# ============================== variable =================

# ++++++++++++++++++++++++++++++ main ++++++++++++++++++++
def status():
    try:
        file_names = os.listdir(path_file+data_shopee);
        status = False;
        file = "shopee.xlsx";
        # Print the list of file names
        for file_name in file_names:
            if(status_run_program):# หยุดทำงาน
                return
            status=file_name==file;
        print("Status : พบไฟล์ ",status)
        return status;
    except Exception as e:
        print("Status : ไม่พบไฟล์ ",e);
# Check_Header
def check_data(path_file):
    try:
        header_check = ['col-xs-2-4 href']
        df = pd.read_excel(path_file)
        is_subset = all(item in df.columns for item in header_check);
        if(status_run_program):# หยุดทำงาน
            return
        print("Check_data : พบข้อมูลทั้งหมดใน Excel ",is_subset);
        return is_subset; 
    except Exception as e:
        print("Check_data : ไม่พบข้อมูลทั้งหมดใน Excel ",e);  
def Check_header(path_file):
    try:
        check_data=[]
        df = pd.read_excel(path_file)
        print(df.columns[0])
        # is_subset = all(item in df.columns for item in header);
        # print("Check_data : พบข้อมูลทั้งหมดใน Excel ",is_subset);
        for i in range(len(header_2)):
            for excel in range(len(df.columns)):
                if(status_run_program):# หยุดทำงาน
                    return
                if(header_2[i]==df.columns[excel]):
                    check_data.append(df.columns[excel]);
        print("Check_data : ข้อมูลที่มีทั้งหมด ");
        return check_data; 
    except Exception as e:
        print("Check_data : ข้อมูล Excel ",e);  

# Read Excell
def postAPI_DB(data,id_shop,title_group,i1,link):
    """
    data: text ที่ทำการ += ในตัวแปร success_data_text
    id_shop : shop1_1_1
    title_group:หมวดหมู่กลุ่ม
    i1:กลุ่มหลัก 1 
    link: link หมวดหลัก
    """
    try:
        if(status_run_program):# หยุดทำงาน
            return
        response = requests.post(
            f"{uri_API}addb?id={id_shop}&&web=shopee&&group={title_group}&&title_group={title_group}&&link={link}",
            headers={
                "Content-type":"application/x-www-form-urlencoded"
            },
            data={
                "data":data
            }
        )
        return response.text
    except:
        return {"status":404,"message":"POST API ERROR."}
def data_process(path_file,i1,i2,i3,group,link):
    try:
        find = pd.read_excel(path_file);
        header = Check_header(path_file)
        data_all=[];
        df = pd.read_excel(path_file)
        num_rows, num_columns = df.shape
        Data_everthing=[];
        success_data_text = ""
        for i in range(num_rows):
            data_process = {
                "product":[],
                "price_product_2":[],
                "price_product_1":[],
                "image_product_1":[],
                "discount":[],
                "image_product_2":[],
                "data_product":[],
                "price_before":[],
                "Emoji":[],
                "sold":[],
                "place":[],
                "Recommended_shops":[],
                "count_review":[],
                "maket":[],
                "group":[]
            }
            data = "Product_"+str(i+1);
            Product = {
                data:{
                }
            }
            # เข้าถึงข้อมูลแต่ละชิ้น
            for j in range(12):
                data_input = str(find[header[j]][i]);
                # print(data_input)
                data_process[header_Values[header[j]]]=data_input;
            Product[data]=data_process;
            Product[data]["maket"] = "shopee";
            Product[data]["group"] = group;
            price_product1 = float(Product[data]["price_product_1"].replace(",",""));
            price_product2 = float(Product[data]["price_product_2"].replace(",",""));
            discount = (Product[data]["discount"]=='nan')and "" or Product[data]["discount"];
            price_product1 = (price_product1<=0)and "0" or price_product1;
            price_product2 = (price_product2<=0)and "0" or price_product2;
            address = (Product[data]["place"]=='nan')and "" or Product[data]["place"];
            sold = (Product[data]["sold"]=='nan')and "" or Product[data]["sold"];
            price_before = (Product[data]["price_before"]=='nan')and "" or Product[data]["price_before"]
            # ***************************ไอดีสินค้าหลัก*************************************
            id_shop = "shop"+str(i1)+"_"+str(i2)+"_"+str(i3);
            # ****************************************************************
            success_data_text += f'APRODUCT:::maket:::{Product[data]["maket"]}, group:::{group}, product:::{Product[data]["product"]}, price_product_2:::{price_product2}, price_product_1:::{price_product1}, image_product_1:::{Product[data]["image_product_1"]}, discount:::{discount}, image_product_2:::{Product[data]["image_product_2"]}, data_product:::{Product[data]["data_product"]}, price_before:::{price_before}, Emoji:::{Product[data]["Emoji"]}, sold:::{sold}, place:::{address}, Recommended_shops:::{Product[data]["Recommended_shops"]}'
            data_all.append(Product);
            success_data = {
                 "id":id_shop,
                 "data":data_all
            }
            # ถ้าข้อมูลครบ 60 ค่อยบันทึก .json และส่ง API
            if(i==num_rows-1):
                # print(success_data_text); #ข้อมูลที่จะส่งไป API
                print(postAPI_DB(success_data_text,id_shop,group,i1,link));
        print("data_process : True")
    except Exception as e:
        print("data_process : False",e)
def Del():
    folder_path = path_file+data_shopee;
    # ลบไฟล์ทั้งหมดในโฟลเดอร์
    for file_name in os.listdir(folder_path):
        if(status_run_program):# หยุดทำงาน
            return
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            staut_working = f"ลบไฟล์ : True";
        except Exception as e:
            print(f"Del_file : False ",e);
Data = [];
def custom_sleep(seconds):
    time.sleep(seconds)
def Scoll():
    custom_sleep(2);
    for i in range(7):
        if(status_run_program):# หยุดทำงาน
            return
        pyautogui.scroll(-750);
        custom_sleep(6);
def click(x,y):
    if(status_run_program):# หยุดทำงาน
        return
    pyautogui.click(x,y);
    custom_sleep(1.5);
def type_and_enter(text):
    controller = keyboard.Controller();
    # controller.type(text);
    if(status_run_program):# หยุดทำงาน
        return
    pyperclip.copy(text)
    ky.press_and_release('ctrl+v')
    custom_sleep(1);
    
def main(x,t,e,t2,e2):
    controller = keyboard.Controller();
    custom_sleep(3);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        return
    # ********************************
    ky.press_and_release('ctrl+t')
    def enter(k):
        for i in range(k):
            if(status_run_program):# หยุดทำงาน
                return
            controller.press(keyboard.Key.enter);
            controller.release(keyboard.Key.enter);
    def tab(t):
        for i in range(t):
            if(status_run_program):# หยุดทำงาน
                return
            controller.press(keyboard.Key.tab);
            controller.release(keyboard.Key.tab);
    # input path
    type_and_enter(x);
    custom_sleep(2);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        return
    # ********************************
    enter(1)
    # Mouse clicked at (1360, 264) with Button.left
    custom_sleep(4);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        return
    # ********************************
    tab(1)
    Scoll();
    ky.press_and_release('ctrl+m');

    custom_sleep(4);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        return
    # ********************************
    # Mouse clicked at (834, 114) with Button.left
    # Mouse clicked at (755, 179) with Button.left
# Mouse clicked at (1006, 88) with Button.left
    ky.press_and_release('F11')
    custom_sleep(4);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        return
    # ********************************
    tab(t);
    custom_sleep(4);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        return
    # ********************************
    enter(e)
    custom_sleep(1);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        return
    # ********************************
    tab(t2);
    custom_sleep(1);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        return
    # ********************************
    enter(e2)
    # Mouse clicked at (1118, 17) with Button.left
    custom_sleep(2);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        return
    # ********************************
    ky.press_and_release('alt+F4')
    # reface
    custom_sleep(1);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        return
    # ********************************
    ky.press_and_release('ctrl+w')
    print("Main : โปรแกรมกำลังทำงาน");
# Change_name
def change_name(k,i,j):
    try:
        path ='.\Data_shopee\data_'+str(k)+'_'+str(i)+'_'+str(j)+'.xlsx'
        path_file_change = path_file+data_shopee+data_shopee_xlsx;
        new_file_name = 'data_'+str(k)+'_'+str(i)+'_'+str(j)+'.xlsx'
        # สร้างเส้นทางสำหรับไฟล์ใหม่
        new_file_path = os.path.join(os.path.dirname(path_file_change), new_file_name);
        # เปลี่ยนชื่อไฟล์
        shutil.move(path_file_change, new_file_path);
        print("Change_name : เปลี่ยนชื่อไฟล์สำเร็จ",path)
        return path;
    except Exception as e:
        print("Change_name : เปลี่ยนชื่อไฟล์ไม่สำเร็จ",e)
# Link_from_json
def get_link():
    try:
        path_here = os.getcwd();
        path_here = os.path.abspath(os.path.join(path_here, os.pardir))
        path = drag_data+data_link;
        with open(path, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
            print("Get_link : พบลิงค์ที่จะทำงาน")
        return data;
    except Exception as e:
        print("Get_link : ไม่พบลิงค์ที่จะทำงาน \t",e);
def run():
        Del();
        # ********************************
        if(status_run_program):# หยุดทำงาน
            return
        # ********************************
        num1=int(data_link_for_shopee_gui[selected_value.get()])
        for k in range(num1,len(data_link_for_shopee)):
            if(status_run_program):# หยุดทำงาน
                return
            print("====== Round [",k+1,"] Working [",data_link_for_shopee[k],"]======");
            Data = get_link();
            num2=0;
            data_all = Data[data_link_for_shopee[k]]["shopee"];
            # try: len(data_all)
            for i in range(len(data_all)):
                    if(status_run_program):# หยุดทำงาน
                        return
                    num2+=1;
                    num3=0;
                    # try:
                    for j in range(9):
                        print("================")
                        data_sum=data_all[i]+"/?page="+str(j);
                        main(data_sum,7,1,0,0);
                        find_shopee = status();
                        if(status_run_program):# หยุดทำงาน
                            return
                        if(find_shopee==True):
                            num3+=1;
                            path = change_name(k+1,num2,num3);
                            print(path);
                            if(check_data(path_file+path)==True):
                                 # ***************************************************การเพิ่ม log ยังไม่สำเร็จ *************************
                                log.addLog("data_%d_%d_%d group:%s : True"%(k+1,num2,num3,data_link_for_shopee[k]))
                                setTreeCommand()
                                # ***************************************************การเพิ่ม log ยังไม่สำเร็จ *************************
                                print("data_%d_%d_%d group:%s : True"%(k+1,num2,num3,data_link_for_shopee[k]));
                                data_process(path_file+path,k+1,num2,num3,data_link_for_shopee[k],data_all[i]);
                            else:
                                print("data_%d_%d_%d group:%s : False"%(k+1,num2,num3,data_link_for_shopee[k]));
                                destination_path = path_file+un_process;
                                shutil.move(path_file+path, destination_path)
                                continue;
                        else:
                            continue;
                        print("For_j : True");
                        print("================");
                    # custom_sleep(120);  
                    # except Exception as e:
                    #     print("For_j",e);
            num1+=1
            # except Exception as e:
            #     print("For_i : ",e);
# ++++++++++++++++++++++++++++++ main ++++++++++++++++++++ 
# +++++++++++++++++++++++++++++++++++++++++++++++ Command GUI button ++++++++++++++++++++++++++++++++++++
def run_system():
    global status_run_program;
    status_run_program = False
    showStatusBot.set("สถาณะการทำงาน : กำลังทำงาน")
    # log.clearLog()
    setTreeCommand()
    t = threading.Thread(target=run)
    t.start();
def stop_program():
    global status_run_program;
    status_run_program= True
    showStatusBot.set("สถาณะการทำงาน : หยุดทำงาน")
    messagebox.showinfo("โปรแกรม'หยุดทำงาน'",f"โปรแกรม'หยุดทำงาน'");
# ****************** button start and stop ***********************************************************
buttom_start = Button(app,text="Start",bg="#9ADE7B",fg="white",command=run_system)
buttom_start.place(x=100,y=10,width=300,height=30)
buttom_stop = Button(app,text="Stop",bg="#7360DF",fg="white",command=stop_program)
buttom_stop.place(x=100,y=50,width=300,height=30)
buttom_stop = Button(app,text="ลบประวัติทั้งหมด",bg="#FF6868",fg="white",command=log.clearLog)
buttom_stop.place(x=190,y=555,width=270,height=30)
# entry = Entry(app, width=40)
# entry.pack(pady=10)  
# ****************** dropdown select group ***********************************************************
options = ['อุปกรณ์-อิเล็กทรอนิกส์', 'อุปกรณ์เสริม-อิเล็กทรอนิกส์', 'ทีวีและเครื่องใช้ในบ้าน','สุขภาพและความงาม','ทารกและของเล่น','ของชำและสัตว์เลี้ยง','บ้านและไลฟ์สไตล์','แฟชั่นและเครื่องประดับผู้หญิง','แฟชั่นและเครื่องประดับผู้ชาย','กีฬาและการเดินทาง','ยานยนต์และรถจักรยานยนต์',"เครื่องประดับ","ตั๋วและบัตรกำนัน"]
def on_dropdown_change(event):
    selected_value = data_link_for_shopee_gui[event.widget.get()]

# ****************** แสดง log ***********************************************************
def setTreeCommand():
    table.delete(*table.get_children())
    data = log.getLog()
    for i in range(len(data)):
        table.insert('','end',values=(i,data[i]))
header_gui = ['loop','group system']
hdsize = [50,400]
table = ttk.Treeview(app,columns=header_gui,show='headings')
table.place(x=20,y=120,height=430)
# header
for h,s in zip(header_gui,hdsize):
    table.heading(h,text=h)
    table.column(h,width=s)
setTreeCommand()
# **************************************************************************************

showStatusBot.set("สถาณะการทำงาน : ยังไม่ทำงาน")
dropdown = ttk.Combobox(app, textvariable=selected_value, values=options)
dropdown.place(x=20,y=90);
titleStatusbot = Label(app,textvariable=showStatusBot)
titleStatusbot.place(x=20,y=560)

text = scrolledtext.ScrolledText(app, wrap=WORD, width=60, height=15)
text.pack(pady=10)
sys.stdout = PrintRedirector(text)
text.place(x=7,y=600)
# Set a default value
dropdown.set(options[0])
# Bind the event handler to the <<ComboboxSelected>> event
dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)
app.mainloop()

#  ++++++++++++++++++++++++++++++++++++ gui +++++++++++++++++++++++++++++


