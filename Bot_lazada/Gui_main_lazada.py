
# from main_lazada import*
from tkinter import *
import tkinter as tk
from tkinter import messagebox,scrolledtext,ttk
import webbrowser,threading,subprocess,sys,shared_module 
# ==================================== Main +++++++++++++++++++++++++++
import requests,os,json,time,pandas as pd,pyautogui,shutil,pyperclip,keyboard as ky
from fnmatch import fnmatch
from pynput import keyboard,mouse
from data_address import address as ad
#  ==================================== Class And varible +++++++++++++++++++++++++++

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
data_link_for_lazada_gui  = {
    'สุขภาพและความงาม':0,
    'แฟชั่นและเครื่องประดับผู้ชาย':1,
    'แฟชั่นและเครื่องประดับผู้หญิง':2,
    'ทีวีและเครื่องใช้ในบ้าน':3,
    'อุปกรณ์-อิเล็กทรอนิกส์':4,
    'อุปกรณ์เสริม-อิเล็กทรอนิกส์':5,
    'ของชำและสัตว์เลี้ยง':6,
    'ทารกและของเล่น':7,
    'ยานยนต์และรถจักรยานยนต์':8,
    'กีฬาและการเดินทาง':9,
    'บ้านและไลฟ์สไตล์':10, 
    "ตั๋วและบัตรกำนัน":11
    }
data_link_for_lazada  = {
     0:'สุขภาพและความงาม',
    1:'แฟชั่นและเครื่องประดับผู้ชาย',
    2:'แฟชั่นและเครื่องประดับผู้หญิง',
    3:'ทีวีและเครื่องใช้ในบ้าน',
    4:'อุปกรณ์-อิเล็กทรอนิกส์',
    5:'อุปกรณ์เสริม-อิเล็กทรอนิกส์',
    6:'ของชำและสัตว์เลี้ยง',
    7:'ทารกและของเล่น',
    8:'ยานยนต์และรถจักรยานยนต์',
    9:'กีฬาและการเดินทาง',
    10:'บ้านและไลฟ์สไตล์', 
    11:"ตั๋วและบัตรกำนัน"
    }
# new_data = [
#     'สุขภาพและความงาม',
#     'แฟชั่นและเครื่องประดับผู้ชาย',
#     'แฟชั่นและเครื่องประดับผู้หญิง',
#     'ทีวีและเครื่องใช้ในบ้าน',
#     'อุปกรณ์-อิเล็กทรอนิกส์',
#     'อุปกรณ์เสริม-อิเล็กทรอนิกส์',
#     'ของชำและสัตว์เลี้ยง',
#     'ทารกและของเล่น',
#     'ยานยนต์และรถจักรยานยนต์',
#     'กีฬาและการเดินทาง',
#     'บ้านและไลฟ์สไตล์', 
#     "ตั๋วและบัตรกำนัน"
# ]
# data_new  = {
#    'สุขภาพและความงาม':0,
#     'แฟชั่นและเครื่องประดับผู้ชาย':1,
#     'แฟชั่นและเครื่องประดับผู้หญิง':2,
#     'ทีวีและเครื่องใช้ในบ้าน':3,
#     'อุปกรณ์-อิเล็กทรอนิกส์':4,
#     'อุปกรณ์เสริม-อิเล็กทรอนิกส์':5,
#     'ของชำและสัตว์เลี้ยง':6,
#     'ทารกและของเล่น':7,
#     'ยานยนต์และรถจักรยานยนต์':8,
#     'กีฬาและการเดินทาง':9,
#     'บ้านและไลฟ์สไตล์':10, 
#     "ตั๋วและบัตรกำนัน":11
# }
header_2 = ['_95X4G href', 'jBwCF src', 'jBwCF src 2'
          , 'RfADt', 'ooOxS',
       '_1cEkb', 'qzqFw', 'oa6ri']
header_Values = {
    '_95X4G href':"product",
    'jBwCF src':"image_product_1",
    'jBwCF src 2':"image_product_2",
    'IcOsH':"discount",
    'RfADt':"data_product", 
    'ooOxS':"price_product",
    '_1cEkb':"sold",
    'qzqFw':"count_review", 
    'oa6ri':"place"
}
Data = [];
#  ==================================== ... +++++++++++++++++++++++++++
# api
uri_API = "https://8f34-14-207-201-178.ngrok-free.app/"
# gui_
font1 = ("Angsana New",25)
app = Tk()
app.title("Lazada")
app.config(bg="#332941") 
app.geometry("500x900+0+0")
# ****************** varible in GUI tk ***********************************************************
selected_value = StringVar()
value_num2 = StringVar()
# selected_value.set()s
showStatusBot = StringVar()
value_to_gui = IntVar()
log = ReadAndWriteLog() 

# path
bot_lazada = r'\Bot_lazada'
path_file = os.getcwd();
drag_data = os.path.abspath(os.path.join(path_file, os.pardir))
data_lazada = r'\Data_lazada';
data_lazada_xlsx = r'\lazada.xlsx';
un_process = r'\Unprocess';
data_link = r'\Data_link\data_link_all.json';
desk_top = 7;
staut_working = "test";


# link_json
def statusLinkJson():
    """status : เช็คไฟล์ว่ามีไฟล์ Lazada ไหม
    Returns:
        Bolean: True
    """
    try:
        file_names = os.listdir(path_file+data_lazada);
        status = False;
        file = "lazada.xlsx";
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
    """
    Check_data : เช็ค Head xlsx ว่ามีสื่งที่ต้องการไหม
    Args:
        path_file String: Path file for find head
    Returns:
        Bolean : True
    """
    try:
        header = ['_95X4G href']
        df = pd.read_excel(path_file)
        if(status_run_program):# หยุดทำงาน
            return
        is_subset = all(item in df.columns for item in header);
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
def postAPI_DB(data,id_shop,title_group,link):
    """
    data: text ที่ทำการ += ในตัวแปร success_data_text
    id_shop : shop1_1_1
    title_group:หมวดหมู่กลุ่ม
    i1:กลุ่มหลัก 1 
    link: link หมวดหลัก
    """
    try:
        response = requests.post(
            f"{uri_API}addb?id={id_shop}&&web=lazada&&title_group={title_group}&&link={link}",
            headers={
                "Content-type":"application/x-www-form-urlencoded"
            },
            data={
                "data":data
            }
        )
        print(response.text)
        return {"status":200,"message":"POST API SUCCESS."}
    except:
        return {"status":404,"message":"POST API ERROR."}
def is_thai(text):
    thai_unicode_range = (0x0E00, 0x0E7F)
    return all(ord(char) in range(thai_unicode_range[0], thai_unicode_range[1] + 1) for char in text)

# process excel file to Json(API)
def data_process(path_file,i1,i2,i3,group,link):
    """
    Process : เพื่อจัดตำแหน่งข้อมูลให้สามารถป้อนเข้า Data Base ได้
    Args:
        path_file: ไฟล์ข้อมูล excel ที่โหลดมาด้วยโปเกบอล อ่านเพื่อแปลงข้อมูลเป็น json
        i1: รอบการทำงานใหญ่ที่สุด ก็คือ หมวดหมู่
        i2: รอบการทำงานกลาง ก็คือ หมวดหมู่ สับย่อยลงมา
        i3: รอบการทำงานเล็กสุด ก็คือ หน้าแต่ละหน้าของสับย่อย ที่เราให้ไปอ่านแล้วกดโหลด
        group: _description_
    """
    try:
        if(status_run_program):# หยุดทำงาน
            return
        header = Check_header(path_file)
        read_excel = pd.read_excel(path_file);
        num_rows, num_columns = read_excel.shape
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
            for j in range(len(header)):
                data_input = str(read_excel[header[j]][i]);
                data_process[header_Values[header[j]]]=data_input;
            # ****************************************************************
            Product = {}
            Product[data]= data_process
            Product[data]["maket"]="lazada"
            Product[data]["group"]=group
            id_shop = f'shop{i1}_{i2}_{i3}'
            # ****************************************************************
            product = Product[data]["product"]
            image_product_1 = Product[data]["image_product_1"]
            image_product_2 = Product[data]["image_product_2"]
            discount = Product[data]["discount"]
            data_product = Product[data]["data_product"]
            price_product = float(Product[data]["price_product"].replace("฿","").replace(",",""))
            price_product = (price_product<=0)and "0" or price_product
            sold = (Product[data]["sold"].split(" ")[0]=="nan")and "0" or Product[data]["sold"].split(" ")[0]
            if is_thai(Product[data]["place"]):
                address = (Product[data]["place"]=='nan')and "" or Product[data]["place"]
            else:
                address = (Product[data]["place"]=='nan')and "" or ad[Product[data]["place"]]
            count_review = (Product[data]["count_review"]=="nan")and "0" or Product[data]["count_review"]
            maket = Product[data]["maket"]
            # ****************************************************************
            success_data_text += f'APRODUCT:::maket:::{maket}, group:::{group}, product:::{product}, price_product_2:::{""}, price_product_1:::{price_product}, image_product_1:::{image_product_1}, discount:::{discount}, image_product_2:::{image_product_2}, data_product:::{data_product}, price_before:::{""}, Emoji:::{""}, sold:::{sold}, place:::{address}, Recommended_shops:::{""}, count_review:::{count_review}'
            # ถ้าข้อมูลครบ 60 ค่อยบันทึก .json และส่ง API
            if(i==num_rows-1):
                print(success_data_text)
                print(postAPI_DB(success_data_text,id_shop,group,link));
    except Exception as e:
        print(e);
# Check_count
def check_data_count(path): 
    try:
        if(status_run_program):# หยุดทำงาน
            return
        header = ['ant-pagination-item 6']
        df = pd.read_excel(path)
        is_subset = all(item in df.columns for item in header);
        print("Status Check_Data_count : พบหน้าเว็บทั้งหมด ",is_subset);
        return is_subset;
    except Exception as e:  
        print("Status Check_Data_count : ไม่พบหน้าเว็บทั้งหมด ",e);

def page():
    try:
        if(status_run_program):# หยุดทำงาน
            return
        path = path_file+data_lazada+data_lazada_xlsx
        df = pd.read_excel(path)
        test ='ant-pagination-item 6'
        num = [];
        num.append(int(df[test][2]))
        os.remove(path);
        print("page_count : พบหน้าเว็บทั้งหมด ",num[0]);
        return num[0];
    except Exception as e:
        print("page_count : ไม่พบหน้าเว็บทั้งหมด ",e);
def Del():
    try:
        if(status_run_program):# หยุดทำงาน
            return
        folder_path = path_file+data_lazada;
        # ลบไฟล์ทั้งหมดในโฟลเดอร์
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                staut_working = f"ลบไฟล์ : True";
            except Exception as e:
                print(f"Del_file : False ",e);
    except:
        pass
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
    pyautogui.click(x,y);
    custom_sleep(1.5);
def type_and_enter(text):
    controller = keyboard.Controller();
    # controller.type(text);
    pyperclip.copy(text)
    if(status_run_program):# หยุดทำงาน
            return
    ky.press_and_release('ctrl+v')
    custom_sleep(1);
# bot is auto click on website
def main(x,t,e,t2,e2):
    # webbrowser.open_new_tab("https://www.lazada.co.th/?spm=a2o4m.searchlistcategory.header.dhome.520251eequOvSC")
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
        path ='\Data_lazada\data_'+str(k)+'_'+str(i)+'_'+str(j)+'.xlsx'
        path_file_change = path_file+data_lazada+data_lazada_xlsx;
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
# run
path_remove = path_file+data_lazada+data_lazada_xlsx    
def run():
    Del();
    if(status_run_program):# หยุดทำงาน
        return
    # ********************************
    num1=int(data_link_for_lazada_gui[selected_value.get()]);
    for k in range(num1,len(data_link_for_lazada)):
        count = 0;
        if(status_run_program):# หยุดทำงาน
            return
        print("====== Round [",k+1,"] Working [",data_link_for_lazada[k],"]======");
        Data = get_link();
        num2=0;
        data_all = Data[data_link_for_lazada[k]]["lazada"];
        value_to_gui.set(len(data_all));
        # try:
        for i in range(len(data_all)):
            # ********************************
            if(status_run_program):# หยุดทำงาน
                return
            # ********************************
            round_click = 3;
            num2+=1;
            num3=0; 
            status_count = False
            main(data_all[i],1,round_click,desk_top,1);
            if(status_run_program):# หยุดทำงาน
                return
            if(statusLinkJson()==False):
                print("Main : ไม่พบไฟล์กรุณาเช็คเส้นทางดาวน์โหลดแล้วลองอีกครั้ง");
                break;
            status_lazada = check_data_count(path_remove);
            if(status_lazada==False):
                round_click = 2;
            for c in range(status_lazada==False):
                print("Main : เกิดข้อพิดพลาดกำลังค้นหาหน้าอีกครั้ง...")
                os.remove(path_remove);
                main(data_all[i],1,round_click,desk_top,1);
                if(status_run_program):# หยุดทำงาน
                    return
                status_lazada = check_data_count(path_remove)
                if(c==2):
                    print("Main : เกิดข้อพิดพลาดไม่สามารถค้นหาหน้าได้กำลังไปลิงค์ถัดไป...");
                    break;
            # try:
            if(status_lazada==True):
                print("Main : ค้นหาหน้าสำเร็จ")
                status_count = check_data_count(path_file+data_lazada+data_lazada_xlsx);
            if(status_count==True):
                count = page()
                for j in range(count):
                    # ********************************
                    if(status_run_program):# หยุดทำงาน
                        return
                    # ********************************
                    print("=======================");
                    data_sum=data_all[i]+"/?page="+str(j+1);
                    main(data_sum,desk_top+1,1,0,0);
                    find_shopee = statusLinkJson();
                    if(find_shopee==True):
                        num3+=1;
                        path = change_name(k+1,num2,num3);
                        if(check_data(path_file+path)==True):
                            # ***************************************************การเพิ่ม log ยังไม่สำเร็จ *************************
                            log.addLog("data_%d_%d_%d group:%s : True"%(k+1,num2,num3,data_link_for_lazada[k]))
                            setTreeCommand()
                            # ***************************************************การเพิ่ม log ยังไม่สำเร็จ *************************
                            print("data_%d_%d_%d group:%s : True"%(k+1,num2,num3,data_link_for_lazada[k]));
                            data_process(path_file+path,k+1,num2,num3,data_link_for_lazada[k],data_all[i]);
                        else:
                            print("data_%d_%d_%d group:%s : False"%(k+1,num2,num3,data_link_for_lazada[k]));
                            destination_path = path_file+un_process;
                            shutil.move(path_file+path, destination_path)
                            continue
                    else:
                        continue;
                    print("=======================");
                custom_sleep(120);
                # else:
                #     continue;
                # print("For_J : True");
        num1+=1;
        # except Exception as e:
        #     print("For_i : ",e)
# +++++++++++++++++++++++++++++++++++++++++++++++ Command GUI button ++++++++++++++++++++++++++++++++++++
def run_system():
    global status_run_program;
    status_run_program = False
    showStatusBot.set("สถาณะการทำงาน : กำลังทำงาน")
    setTreeCommand()
    t = threading.Thread(target=run)
    t.start();
def stop_program():
    global status_run_program;
    status_run_program= True
    showStatusBot.set("สถาณะการทำงาน : หยุดทำงาน")
    messagebox.showinfo("โปรแกรม'หยุดทำงาน'",f"โปรแกรม'หยุดทำงาน'");
# ****************** button start and stop ***********************************************************
buttom_start = Button(app,text="start bot",bg="#9ADE7B",fg="white",command=run_system)
buttom_start.place(x=100,y=10,width=300,height=30)
buttom_stop = Button(app,text="stop bot",bg="#7360DF",fg="white",command=stop_program)
buttom_stop.place(x=100,y=50,width=300,height=30)
buttom_stop = Button(app,text="ลบประวัติทั้งหมด",bg="#FF6868",fg="white",command=log.clearLog)
buttom_stop.place(x=190,y=555,width=270,height=30)
# entry = Entry(app, width=40)
# entry.pack(pady=10)  
# ****************** dropdown select group ***********************************************************
options = ['สุขภาพและความงาม',
    'แฟชั่นและเครื่องประดับผู้ชาย',
    'แฟชั่นและเครื่องประดับผู้หญิง',
    'ทีวีและเครื่องใช้ในบ้าน',
    'อุปกรณ์-อิเล็กทรอนิกส์',
    'อุปกรณ์เสริม-อิเล็กทรอนิกส์',
    'ของชำและสัตว์เลี้ยง',
    'ทารกและของเล่น',
    'ยานยนต์และรถจักรยานยนต์',
    'กีฬาและการเดินทาง',
    'บ้านและไลฟ์สไตล์', 
    "ตั๋วและบัตรกำนัน"
]
value_link = get_link();
selected_value_num_2 = tk.StringVar()
value_num2 = StringVar()

# ****************** แสดง log ***********************************************************
def setTreeCommand():
    table.delete(*table.get_children())
    data = log.getLog()
    for i in range(len(data)):                         
        table.insert('','end',values=(i,data[i]))
header_gui = ['loop','group system']
hdsize = [50,400]
table = ttk.Treeview(app,columns=header_gui,show='headings')
table.place(x=20,y=120,height=400)
# header
for h,s in zip(header_gui,hdsize):
    table.heading(h,text=h)
    table.column(h,width=s)
setTreeCommand()
# ************************* Function*************************

def on_dropdown_change(event):
    selected_value.set(event.widget.get())
    number_dropdown_2();
def on_dropdown_change_num2(event):
    selected_num2 = event.widget.get()
    value_num2.set(selected_num2)
    print(value_num2.get())
def number_dropdown_2():
    # ตรวจสอบว่ามีค่าที่ถูกเลือกใน dropdown แรกหรือไม่
    selected = selected_value.get()
    print(selected_value.get())
    options_2=[str(i) for i in range(1,1+len(value_link[selected]['lazada']))]
    selected_value_num_2.set(options_2[0])
    print(selected_value_num_2.get());
    dropdown_num_2['values'] = options_2
    print(len(value_link[selected]['lazada']))

# *************************************************************

showStatusBot.set("สถาณะการทำงาน : ยังไม่ทำงาน")
dropdown = ttk.Combobox(app, textvariable=selected_value, values=options)
dropdown.place(x=20,y=90);
titleStatusbot = Label(app,textvariable=showStatusBot)
titleStatusbot.place(x=20,y=560)
dropdown.set(options[0])
dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)

# *************************************************************
# num_2

dropdown_num_2 = ttk.Combobox(app, textvariable=selected_value_num_2 ,values=selected_value_num_2);
dropdown_num_2.place(width=50, x=175, y=90)
dropdown_num_2.bind("<<ComboboxSelected>>", on_dropdown_change_num2);

# *************************************************************
# num3
selected_value_num_3 = [str(i) for i in range(10)]
dropdown_num_3 = ttk.Combobox(app, textvariable=selected_value_num_3 ,values=selected_value_num_3);
dropdown_num_3.place(width=50, x=230, y=90)
# dropdown_num_.bind("<<ComboboxSelected>>", on_dropdown_change_num3);

# *************************************************************
# terminal
text = scrolledtext.ScrolledText(app, wrap=WORD, width=60, height=15)
text.pack(pady=10)
sys.stdout = PrintRedirector(text)
text.place(x=7,y=600)
# Set a default value

# Bind the event handler to the <<ComboboxSelected>> event

app.mainloop()

#  ++++++++++++++++++++++++++++++++++++ gui +++++++++++++++++++++++++++++


