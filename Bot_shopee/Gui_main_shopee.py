# ++++++++++++++++++++++++++++++ gui ++++++++++++++++++++ import 
from tkinter import *
import tkinter as tk
from tkinter import messagebox,scrolledtext,ttk
import webbrowser,threading,subprocess,sys
from PIL import ImageGrab
# ++++++++++++++++++++++++++++++ gui ++++++++++++++++++++

# ++++++++++++++++++++++++++++++ main ++++++++++++++++++++ import 
import requests,os,json,time,pandas as pd,pyautogui,shutil,pyperclip,keyboard as ky , datetime as dt
from datetime import datetime
from fnmatch import fnmatch
from pynput import keyboard,mouse
from data_address import address as ad
# ++++++++++++++++++++++++++++++ main ++++++++++++++++++++
# dependency 'openpyxl'.  Use pip or conda to install openpyxl.
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
setting_insert = open('./log/setting.txt',mode='r',encoding='utf-8');
# path
bot_shopee = r'\Bot_shopee';
path_file = os.getcwd();
drag_data = os.path.abspath(os.path.join(path_file, os.pardir));
path_project = os.getcwd()+f'\\imag'+'\\Error.png';
data_shopee = r'\Data_shopee';
data_shopee_xlsx = r'\shopee.xlsx';
un_process = r'\Unprocess';
data_link = r'\Data_link\data_link_all.json';


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
    0:'อุปกรณ์-อิเล็กทรอนิกส์',
    1:'อุปกรณ์เสริม-อิเล็กทรอนิกส์',
    2:'ทีวีและเครื่องใช้ในบ้าน',
    3:'สุขภาพและความงาม',
    4:'ทารกและของเล่น',
    5:'ของชำและสัตว์เลี้ยง',
    6:'บ้านและไลฟ์สไตล์',
    7:'แฟชั่นและเครื่องประดับผู้หญิง',
    8:'แฟชั่นและเครื่องประดับผู้ชาย',
    9:'กีฬาและการเดินทาง',
    10:'ยานยนต์และรถจักรยานยนต์', 
    11:"ตั๋วและบัตรกำนัน"
    }
options = ['อุปกรณ์-อิเล็กทรอนิกส์',
    'อุปกรณ์เสริม-อิเล็กทรอนิกส์',
    'ทีวีและเครื่องใช้ในบ้าน',
    'สุขภาพและความงาม',
    'ทารกและของเล่น',
    'ของชำและสัตว์เลี้ยง',
    'บ้านและไลฟ์สไตล์',
    'แฟชั่นและเครื่องประดับผู้หญิง',
    'แฟชั่นและเครื่องประดับผู้ชาย',
    'กีฬาและการเดินทาง',
    'ยานยนต์และรถจักรยานยนต์', 
    "ตั๋วและบัตรกำนัน"
]
# ============================== variable =================
# ============================== variable ================= gui
font1 = ("Angsana New",25)
app = Tk()
app.title("Shopee")
app.config(bg="#332941") 
app.geometry("500x900-0+0")

selected_value = StringVar()
value_num2 = StringVar()
# selected_value.set()s
showStatusBot = StringVar()
value_to_gui = IntVar()
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
    "ตั๋วและบัตรกำนัน":11
}
# ============================== variable =================
# ++++++++++++++++++++++++++++++ main ++++++++++++++++++++
# ==================================================================
def setting():
    data = setting_insert.readlines()
    data_setting = []
    for i in range(len(data)):
        data_setting.append(data[i].replace('\n','').split('=')[1]);
    return data_setting;
# ============================== variable_from_text =================
data_setting = setting();
uri_API=data_setting[0]
desk_top = int(data_setting[1])
px_scroll = int(data_setting[2])
round_scroll = int(data_setting[3])
key_progemon = data_setting[4];
token_line  = data_setting[5];
# ============================== Api Line ====================================

def data_image():
    try:
        ImageGrab.grab().save(path_project)
    except Exception as e:
        print(e)

def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload);

def notifyFile(filename):
    file = {'imageFile':open(filename,'rb')}
    payload = {'message': '\nรูปจากความผิดพลาด: '}
    return _lineNotify(payload,file)

def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

def _lineNotify(payload,file=None):
    url = 'https://notify-api.line.me/api/notify'
	#EDIT
    headers = {'Authorization':'Bearer '+token_line}
    return requests.post(url, headers=headers , data = payload, files=file)

# ====================================================================================
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
def is_thai(text):
    thai_unicode_range = (0x0E00, 0x0E7F)
    return all(ord(char) in range(thai_unicode_range[0], thai_unicode_range[1] + 1) for char in text)
def postAPI_DB(data,id_shop,link,date,time,website,group):
    """
    data: text ที่ทำการ += ในตัวแปร success_data_text
    id_shop : shop1_1_1
    title_group:หมวดหมู่กลุ่ม
    i1:กลุ่มหลัก 1 
    link: link หมวดหลัก
    """
    try:
        response = requests.post(
            f'{uri_API}addb?idshop={id_shop}&&link={link}&&date={date}&&time={time}&&website={website}&&group={group}',
            headers={
                "Content-type":"application/x-www-form-urlencoded"
            },
            data={
                "data":data
            }
        )
        return response.status_code
    except:
        return {"status":404,"message":"POST API ERROR."}
def convert_to_integer(s):
    if 'พัน' in s:
        return int(float(s.replace('พัน', '')) * 1000);
    elif 'ล้าน' in s:
        return int(float(s.replace('ล้าน', '')) * 1000000);
    else:
        return int(s)
    

def get_datetime():
  now = datetime.now()
  date_str = now.strftime("%Y-%m-%d")
  time_str = now.strftime("%H:%M:%S")
  return {
    "date": date_str,
    "time": time_str,
}
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
            dt = get_datetime()
            Date = dt['date']
            Time = dt['time']
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
                'gruop':[],
                'date':[],
                'time':[],
                'link':[]
            }
            data = "Product_"+str(i+1);
            Product = {
                data:{
                }
            }
            # เข้าถึงข้อมูลแต่ละชิ้น
            for j in range(len(header)):
                data_input = str(find[header[j]][i]);
                # print(data_input)
                data_process[header_Values[header[j]]]=data_input;
            Product[data]=data_process;
            Product[data]["maket"] = "shopee";
            Product[data]["group"] = group;
            # ****************************************************************
            Product[data]['date'] = Date
            Product[data]['time'] = Time
            Product[data]['link'] = link
            # ****************************************************************
            price_product1 = float(Product[data]["price_product_1"].replace(",",""));
            price_product2 = float(Product[data]["price_product_2"].replace(",",""));
            discount = (Product[data]["discount"]=='nan')and " " or Product[data]["discount"];
            price_product1 = (price_product1<=0)and "0" or price_product1;
            price_product2 = (price_product2<=0)and "0" or price_product2;
            if is_thai(Product[data]["place"]):
                address = (Product[data]["place"]=='nan')and " " or Product[data]["place"];
                address=address.replace("จังหวัด","");
            else:
                address = (Product[data]["place"]=='nan')and " " or ad[Product[data]["place"]]
            if(len(Product[data]["sold"])>0):
                sold = (Product[data]["sold"]=='nan')and " " or Product[data]["sold"];
            else:
                sold = "0"
            if("ขายแล้ว" in sold):
                sold = convert_to_integer(sold.split(" ")[1])
            price_before = (Product[data]["price_before"]=='nan')and " " or Product[data]["price_before"]
            # ***************************ไอดีสินค้าหลัก*************************************
            id_shop = "shop"+str(i1)+"_"+str(i2)+"_"+str(i3);
            # ****************************************************************
            data_all.append(Product);
            # ถ้าข้อมูลครบ 60 ค่อยบันทึก .json และส่ง API
            success_data_text += f'APRODUCT:::maket:::{Product[data]["maket"]},'
            success_data_text += f'group:::{group},'
            success_data_text += f'product:::{Product[data]["product"]},'
            success_data_text += f'price_product_2:::{price_product2},' 
            success_data_text += f'price_product_1:::{price_product1},'
            success_data_text += f'image_product_1:::{Product[data]["image_product_1"]},'
            success_data_text += f'discount:::{discount},'
            success_data_text += f'image_product_2:::{Product[data]["image_product_2"]},'
            success_data_text += f'data_product:::{Product[data]["data_product"]},'
            success_data_text += f'price_before:::{price_before},'
            success_data_text += f'Emoji:::{Product[data]["Emoji"]},'
            success_data_text += f'sold:::{sold},'
            success_data_text += f'place:::{address},'
            success_data_text += f'Recommended_shops:::{Product[data]["Recommended_shops"]},'
            success_data_text += f'date:::{Product[data]["date"]},'
            success_data_text += f'time:::{Product[data]["time"]},'
            success_data_text += f'link:::{Product[data]["link"]}'

        status_api ="";
        error_api=False
        if(i==num_rows-1):
            # print(success_data_text);
            status_api = str(postAPI_DB(success_data_text,id_shop,link,Date,Time,'Shopee',group));
            print(status_api);
        if(status_api=="200"):
            error_api=True;
        else:
            error_api=False;
        print("data_process : True");
        if(error_api==False):

            print(lineNotify('\nShopee: Api_Error \nGroup: '+str(group)+'\nId: '+str(group)+"_"+str(i2+1)+"_"+str(i3)+'\nLink: '+link),notifyFile(path_project).text,lineNotify("\nShopee: Stop"));  
        return error_api;
 
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
    for i in range(round_scroll):
        if(status_run_program):# หยุดทำงาน
            return
        pyautogui.scroll(px_scroll);
        custom_sleep(7);
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
    ky.press_and_release(key_progemon);

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
    data_image()
    custom_sleep(1);
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
            #=================== start ======================
            
            #================================================
            if(status_run_program):# หยุดทำงาน
                return
            print("====== Round [",k+1,"] Working [",data_link_for_shopee[k],"]======");
            Data = get_link();
            data_all = Data[data_link_for_shopee[k]]["shopee"];
             # +++++++++++++++++++++++++++++++++++++++++++++++ Show_Status ++++++++++++++++++++++++++++++++++++
            Working.set(str(data_link_for_shopee[k])+" _ "+str(value_num2.get())+" _ "+str(value_num3.get()));
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            print(lineNotify('\nShopee: Working \nGroup: '+data_link_for_shopee[k]+'\nId: '+str(data_link_for_shopee[k])+"_"+str(value_num2.get())+"_"+str(value_num3.get())));
            # try: len(data_all)
            num2=(int(value_num2.get())-1);
            for i in range(num2,len(data_all)):
                    # len(data_all)
                    if(status_run_program):# หยุดทำงาน
                        return
                    num3=0;
                    # try:
                    num3 = int(value_num3.get())
                     # +++++++++++++++++++++++++++++++++++++++++++++++ Show_Status ++++++++++++++++++++++++++++++++++++
                    Working.set(str(data_link_for_shopee[k])+"_"+str(num2+1)+"_"+str(value_num3.get()));
                    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    error = 0;
                    while(num3<9):
                        if(error == 3):

                            print(lineNotify('\nShopee: Error \nGroup: '+str(data_link_for_shopee[k])+'\nId: '+str(data_link_for_shopee[k])+"_"+str(num2+1)+"_"+str(num3)+'\nLink: '+data_sum),notifyFile(path_project).text,lineNotify("\nShopee: Stop"));
                            log.addLog("%s_%d_%d False"%(data_link_for_shopee[k],num2+1,num3))
                            print("%s_%d_%d True"%(data_link_for_shopee[k],num2+1,num3));
                            destination_path = path_file+un_process;
                            shutil.move(path_file+path,destination_path)
                            os.remove(path_project);
                            error=0;
                            return
                        
                        print("================");
                        # +++++++++++++++++++++++++++++++++++++++++++++++ Show_Status ++++++++++++++++++++++++++++++++++++
                        Working.set(str(data_link_for_shopee[k])+"_"+str(num2+1)+"_"+str(num3));
                        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                        data_sum=data_all[i]+str(num3);
                        main(data_sum,desk_top,1,0,0);
                        find_shopee = status();
                        if(status_run_program):# หยุดทำงาน
                            return
                        if(find_shopee==True):
                            path = change_name(k+1,num2+1,num3);
                            print(path);
                            if(check_data(path_file+path)==True):
                                print("%s_%d_%d True"%(data_link_for_shopee[k],num2+1,num3));
                                status_api = data_process(path_file+path,k+1,num2,num3,data_link_for_shopee[k],data_sum);
                                if(status_api==False):
                                    return
                                 # ***************************************************การเพิ่ม log ยังไม่สำเร็จ *************************
                                log.addLog("%s_%d_%d True"%(data_link_for_shopee[k],num2+1,num3))
                                setTreeCommand()
                                # ***************************************************การเพิ่ม log ยังไม่สำเร็จ *************************
                                num3+=1;
                            else:
                                error+=1;
                                continue
                        else:

                            print(lineNotify('\nShopee: ไม่พบไฟล์ \nGroup: '+str(data_link_for_shopee[k])+'\nId: '+str(data_link_for_shopee[k])+"_"+str(num2+1)+"_"+str(num3)+'\nLink: '+data_sum),notifyFile(path_project).text,lineNotify("\nShopee: Stop"));
                            return
                        print("For_j : True");
                        print("================");
                    print(lineNotify('\nShopee: Success Id \nGroup: '+str(data_link_for_shopee[k])+'\nId: '+str(data_link_for_shopee[k])+"_"+str(num2+1)+"_"+str(num3)))
                    num2+=1;
                    value_num3.set(0)
                    if(num2!=len(data_all)):
                        print(lineNotify('\nShopee: Next Id \nGroup: '+str(data_link_for_shopee[k])+'\nId: '+str(data_link_for_shopee[k])+"_"+str(num2+1)+"_"+str(value_num3.get())))

                   
                    # custom_sleep(120);  
                    # except Exception as e:
                    #     print("For_j",e);
            num1+=1;
            print(lineNotify('\nShopee: Success Group \nGroup: '+str(data_link_for_shopee[k])+'\nId: '+str(data_link_for_shopee[k])+"_"+str(num2+1)+"_"+str(num3)))
            value_num2.set(1)
            print(lineNotify('\nShopee: Next Group \nGroup: '+str(data_link_for_shopee[num1])+'\nId: '+str(data_link_for_shopee[num1])+"_"+str(value_num2.get())+"_"+str(value_num3.get())))
            # except Exception as e:
            #     print("For_i : ",e);
# ++++++++++++++++++++++++++++++ main ++++++++++++++++++++ 
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
buttom_start.place(x=25,y=10,width=150,height=30)
buttom_stop = Button(app,text="stop bot",bg="#7360DF",fg="white",command=stop_program)
buttom_stop.place(x=25,y=50,width=150,height=30)
buttom_stop = Button(app,text="ลบประวัติทั้งหมด",bg="#FF6868",fg="white",command=log.clearLog)
buttom_stop.place(x=190,y=555,width=270,height=30)
# entry = Entry(app, width=40)
# entry.pack(pady=10)  

# ****************** variable ***********************************************************

value_link = get_link();
selected_value_num_2 = StringVar()
selected_value_num_3 = StringVar()
value_num2 = StringVar()
value_num2.set(1)
check_count_gui = StringVar();
check_count_gui.set(0);
value_num3=StringVar();
value_num3.set(0);
Working = StringVar();
selected_value.set('สุขภาพและความงาม')
# Working.set(str(selected_value.get())+"_"+str(value_num2.get())+"_"+str(value_num3.get()));

# ****************** แสดง log ***********************************************************
def setTreeCommand():
    table.delete(*table.get_children())
    data = log.getLog()
    for i in range(len(data)-1,-1,-1):                         
        table.insert('','end',values=(i,data[i]));

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

def Set_value_Working():
    Working.set(str(selected_value.get())+"_"+str(value_num2.get())+"_"+str(value_num3.get()))
def on_dropdown_change(event):
    selected_value.set(event.widget.get())
    value_num2.set(1)
    value_num3.set(0);
    Set_value_Working()
    number_dropdown_2();
    number_dropdown_3()

def on_dropdown_change_num2(event):
    selected_num2 = event.widget.get()
    value_num2.set(selected_num2)
    Set_value_Working()
    print(value_num2.get())

def on_dropdown_change_num3(event):
    value_num3.set(event.widget.get())
    Set_value_Working()
    print(value_num3.get());

def number_dropdown_2():
    # ตรวจสอบว่ามีค่าที่ถูกเลือกใน dropdown แรกหรือไม่
    selected = selected_value.get()
    print(selected_value.get())
    options_2=[str(i) for i in range(1,1+len(value_link[selected]['shopee']))]
    selected_value_num_2.set(options_2[0])
    print(selected_value_num_2.get());
    dropdown_num_2['values'] = options_2
    print(len(value_link[selected]['shopee']));

def number_dropdown_3():
    # ตรวจสอบว่ามีค่าที่ถูกเลือกใน dropdown แรกหรือไม่
    selected = selected_value.get()
    print(selected_value.get())
    options_3= [str(i) for i in range(0,9)]
    selected_value_num_3.set(options_3[0])
    print(selected_value_num_3.get());
    dropdown_num_3['values'] = options_3
    print(len(value_link[selected]['shopee']));

def dropdown_value_num3(value):
    selected_value_num_3 = [str(i) for i in range(value)]
    dropdown_num_3 = ttk.Combobox(app, textvariable=selected_value_num_3 ,values=selected_value_num_3);
    dropdown_num_3.place(width=50, x=230, y=90)

# *************************************************************
showStatusBot.set("สถาณะการทำงาน : ยังไม่ทำงาน")
dropdown = ttk.Combobox(app, textvariable=selected_value,values=options);
dropdown.place(x=20,y=90);
titleStatusbot = Label(app,textvariable=showStatusBot)
titleStatusbot.place(x=20,y=560)
show_link_working = Label(app,textvariable=Working,font=36);
show_link_working.place(x=200,y=20,width=280,height=50);
dropdown.set(options[0])
dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)

# *************************************************************
# num_2
dropdown_num_2 = ttk.Combobox(app, textvariable=selected_value_num_2 ,values=selected_value_num_2);
dropdown_num_2.place(width=50, x=175, y=90)
dropdown_num_2.bind("<<ComboboxSelected>>", on_dropdown_change_num2);

# *************************************************************
# num3

dropdown_num_3 = ttk.Combobox(app, textvariable=selected_value_num_3 ,values=selected_value_num_3);
dropdown_num_3.place(width=50, x=230, y=90)
dropdown_num_3.bind("<<ComboboxSelected>>", on_dropdown_change_num3);
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

