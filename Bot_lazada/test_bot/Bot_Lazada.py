
# from main_lazada import*
from tkinter import *
import tkinter as tk
from tkinter import messagebox,scrolledtext,ttk
import webbrowser,threading,subprocess,sys,math
from PIL import ImageGrab
# ==================================== Main +++++++++++++++++++++++++++
import requests,os,json,time,pandas as pd,pyautogui,shutil,pyperclip,keyboard as ky , datetime as dt
from datetime import datetime
from fnmatch import fnmatch
from pynput import keyboard,mouse
from data_address import address as ad
#  ==================================== Thing_as_update +++++++++++++++++++++++++++
"""
    !!
    8/2/67
    Thing_add_in_main
    - Thing add id in product and date in product and Time in porduct for send by Api to database!
    - Delate this word 'จังหวัด' before will send by api to data base!    

    Thing_add_in_Gui
    - Arrange Bigcast Ex 'สุขภาพและความงาม' Arrange same website of pol!
    - Add id data_[]_[]_[] type real time!
    -
    !!
    !!But have to carefull Bug!!
"""
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
data_link_for_lazada  = {
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
    
}
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
    'ยานยนต์และรถจักรยานยนต์':10, 
   
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
  
]
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
header_2 = ['_95X4G href', 'Image', 'jBwCF src 2'
          , 'Data', 'Price',
       'Sold', 'Amount', 'Place']
header_Values = {
    '_95X4G href':"product",
    'Image':"image_product_1",
    'jBwCF src 2':"image_product_2",
    'IcOsH':"discount",
    'Data':"data_product", 
    'Price':"price_product",
    'Sold':"sold",
    'Amount':"count_review", 
    'Place':"place"
}
Data = [];
#  ==================================== ... +++++++++++++++++++++++++++
# Setting
setting_insert = open('./log/setting.txt',mode='r',encoding='utf-8');
# gui_
font1 = ("Angsana New",25)
app = Tk()
app.title("Lazada")
app.geometry("500x900-0+0")
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
path_project = os.getcwd()+f'\\imag'+'\\Error.png';
data_lazada = r'\Data_lazada';
data_lazada_xlsx = r'\lazada.xlsx';
un_process = r'\Unprocess';
data_link = r'\Data_link\data_link_all.json';
staut_working = "test";



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
                print(lineNotify("\nLazada: Stop"));
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
            print(lineNotify("\nLazada: Stop"));
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
                    print(lineNotify("\nLazada: Stop"));
                    return
                if(header_2[i]==df.columns[excel]):
                    check_data.append(df.columns[excel]);
        print("Check_data : ข้อมูลที่มีทั้งหมด ");
        return check_data; 
    except Exception as e:
        print("Check_data : ข้อมูล Excel ",e); 

# Read Excell
def postAPI_DB(data,id_shop,link,date,time,website,group):
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
        return response
    except:
        return {"status":404,"message":"POST API ERROR."}
def is_thai(text):
    thai_unicode_range = (0x0E00, 0x0E7F)
    return all(ord(char) in range(thai_unicode_range[0], thai_unicode_range[1] + 1) for char in text)
def get_datetime():
  now = datetime.now()
  date_str = now.strftime("%Y-%m-%d")
  time_str = now.strftime("%H:%M:%S")
  return {
    "date": date_str,
    "time": time_str,
}
def convert_to_integer(s):
    if 'k' or 'k+' in s:
        sum2 = (s.replace(' ชิ้น',''));
        sum3 = (sum2.replace('k+',''));
        sum3 = (sum3.replace('K',''));
        return float(sum3)*1000;
    elif '9,999+' in s:
        sum2 = (s.replace(' ชิ้น',''));
        sum3 = (sum2.replace('+',''));
        return float(sum3.replace(',',''))+1;
    else:
        return float(s.replace(' ชิ้น',''))
            
            

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
        header = Check_header(path_file)
        read_excel = pd.read_excel(path_file);
        num_rows, num_columns = read_excel.shape
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
            for j in range(len(header)):
                data_input = str(read_excel[header[j]][i]);
                data_process[header_Values[header[j]]]=data_input;
            # ****************************************************************
            Product = {}
            Product[data]= data_process
            Product[data]["maket"]="lazada"
            Product[data]["group"]=group
            Product[data]['date'] = Date
            Product[data]['time'] = Time
            Product[data]['link'] = link
            id_shop = f'shop{i1}_{i2}_{i3}'

            # ****************************************************************
            product = Product[data]["product"]
            image_product_1 = Product[data]["image_product_1"]
            image_product_2 = Product[data]["image_product_2"]
            discount = Product[data]["discount"]
            data_product = Product[data]["data_product"]
            price_product = float(Product[data]["price_product"].replace("฿","").replace(",",""))
            price_product = (price_product<=0)and "0" or price_product
            if(len(Product[data]["sold"])>0):
                sold = (Product[data]["sold"].split(" ")[0]=="nan")and "0" or Product[data]["sold"].split(" ")[0];
            else:
                sold = "0"
            sold = convert_to_integer(sold);
            if is_thai(Product[data]["place"]):
                address = (Product[data]["place"]=='nan')and "" or Product[data]["place"]
            else:
                address = (Product[data]["place"]=='nan')and "" or ad[Product[data]["place"]]
            if 'จังหวัด' in address:
                address.replace("จังหวัด","")
            count_review = (Product[data]["count_review"]=="nan")and "0" or Product[data]["count_review"]
            maket = Product[data]["maket"]
            # ****************************************************************
            success_data_text += f'APRODUCT:::maket:::{maket},'
            success_data_text += f'group:::{group},'
            success_data_text += f'product:::{product},'
            success_data_text += f'price_product_2:::{""},' 
            success_data_text += f'price_product_1:::{price_product},'
            success_data_text += f'image_product_1:::{image_product_1},'
            success_data_text += f'discount:::{discount},'
            success_data_text += f'image_product_2:::{image_product_2},'
            success_data_text += f'data_product:::{data_product},'
            success_data_text += f'price_before:::{""},'
            success_data_text += f'Emoji:::{""},'
            success_data_text += f'sold:::{sold},'
            success_data_text += f'place:::{address},'
            success_data_text += f'Recommended_shops:::{""},'
            success_data_text += f'count_review:::{count_review},'
            success_data_text += f'date:::{Product[data]["date"]},'
            success_data_text += f'time:::{Product[data]["time"]},'
            success_data_text += f'link:::{Product[data]["link"]}'
            # ถ้าข้อมูลครบ 60 ค่อยบันทึก .json และส่ง API
            status_api = "";
            error_api = False;
        if(i==num_rows-1):
            for i in range(0,not error_api,3):
                status_api = postAPI_DB(success_data_text,id_shop,link,Date,Time,'Lazada',group);
                print(status_api.status_code);
                if(status_api.status_code==200):
                    error_api = True;
                    break
                else:
                    error_api = False;
            if(not error_api):
                print(lineNotify('\nLazada: Api_Error \nGroup: '+str(group)+'\nId: '+str(group)+"_"+str(i2+1)+"_"+str(i3)+'\nLink: '+link),notifyFile(path_project).text,lineNotify("\nLazada: Stop"));  
            return error_api;

    except Exception as e:
        print(e);
# Check_count
def check_data_count(path): 
    try:
        if(status_run_program):# หยุดทำงาน
            print(lineNotify("\nLazada: Stop"));
            return
        header = ['ant-pagination-item']
        df = pd.read_excel(path)
        is_subset = all(item in df.columns for item in header);
        print("Status Check_Data_count : พบหน้าเว็บทั้งหมด ",is_subset);
        return is_subset;
    except Exception as e:  
        print("Status Check_Data_count : ไม่พบหน้าเว็บทั้งหมด ",e);
def page():
    try:
        path = path_file+data_lazada+data_lazada_xlsx
        df = pd.read_excel(path)
        head_xlsx ='ant-pagination-item '
        num = [];
        j=0;
        for i in range(0,7):
            if head_xlsx+str(i) in df :
                count = df[head_xlsx+str(i)]
                while(True):
                    if not (math.isnan(count[j])) or j==10:
                        num.append(int(count[j]));
                        break;
                    j+=1;
        os.remove(path);
        print("page_count : พบหน้าเว็บทั้งหมด ",max(num));
        return max(num);
    except Exception as e:
        print("page_count : ไม่พบหน้าเว็บทั้งหมด ",e);
def Del():
    try:
        if(status_run_program):# หยุดทำงาน
            print(lineNotify("\nLazada: Stop"));
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
    for i in range(round_scroll):
        if(status_run_program):# หยุดทำงาน
            print(lineNotify("\nLazada: Stop"));
            return
        pyautogui.scroll(px_scroll);
        custom_sleep(6);
def click(x,y):
    pyautogui.click(x,y);
    custom_sleep(1.5);
def type_and_enter(text):
    controller = keyboard.Controller();
    # controller.type(text);
    pyperclip.copy(text)
    if(status_run_program):# หยุดทำงาน
            print(lineNotify("\nLazada: Stop"));
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
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    ky.press_and_release('ctrl+t')
    def enter(k):
        for i in range(k):
            if(status_run_program):# หยุดทำงาน
                print(lineNotify("\nLazada: Stop"));
                return
            controller.press(keyboard.Key.enter);
            controller.release(keyboard.Key.enter);
    def tab(t):
        for i in range(t):
            if(status_run_program):# หยุดทำงาน
                print(lineNotify("\nLazada: Stop"));
                return
            controller.press(keyboard.Key.tab);
            controller.release(keyboard.Key.tab);
    # input path
    type_and_enter(x);
    custom_sleep(2);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************          
    enter(1)
    # Mouse clicked at (1360, 264) with Button.left
    custom_sleep(4);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    tab(1)
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    data_image()
    custom_sleep(1);
    pyautogui.moveTo(100, 500, duration=0.1) 
    Scoll();
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    ky.press_and_release(key_progemon);

    custom_sleep(4);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    # Mouse clicked at (834, 114) with Button.left
    # Mouse clicked at (755, 179) with Button.left
# Mouse clicked at (1006, 88) with Button.left
    ky.press_and_release('F11')
    custom_sleep(4);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    tab(t);
    custom_sleep(4);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    enter(e)
    custom_sleep(1);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    tab(t2);
    custom_sleep(1);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    enter(e2)
    # Mouse clicked at (1118, 17) with Button.left
    custom_sleep(2);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    ky.press_and_release('alt+F4')
    # reface
    custom_sleep(1);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************

    ky.press_and_release('ctrl+w');
    custom_sleep(4);
    print("Main : โปรแกรมกำลังทำงาน");
def main3(x,t,e,t2,e2):
    # webbrowser.open_new_tab("https://www.lazada.co.th/?spm=a2o4m.searchlistcategory.header.dhome.520251eequOvSC")
    controller = keyboard.Controller();
    custom_sleep(3);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    ky.press_and_release('ctrl+t')
    def enter(k):
        for i in range(k):
            if(status_run_program):# หยุดทำงาน
                print(lineNotify("\nLazada: Stop"));
                return
            controller.press(keyboard.Key.enter);
            controller.release(keyboard.Key.enter);
    def tab(t):
        for i in range(t):
            if(status_run_program):# หยุดทำงาน
                print(lineNotify("\nLazada: Stop"));
                return
            controller.press(keyboard.Key.tab);
            controller.release(keyboard.Key.tab);
    # input path
    pyautogui.moveTo(100, 500, duration=0.1) 
    type_and_enter(x);
    custom_sleep(2);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************          
    enter(1)
    # Mouse clicked at (1360, 264) with Button.left
    custom_sleep(4);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    tab(1)
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    data_image()
    ky.press_and_release(key_progemon);
    custom_sleep(2);
    ky.press_and_release('F11')
    custom_sleep(4);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    tab(t);
    custom_sleep(4);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    enter(e)
    custom_sleep(1);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    tab(t2);
    custom_sleep(1);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    enter(e2)
    # Mouse clicked at (1118, 17) with Button.left
    custom_sleep(2);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    ky.press_and_release('alt+F4')
    # reface
    custom_sleep(1);
    # ********************************
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************

    ky.press_and_release('ctrl+w');
    custom_sleep(4);
    print("Main : โปรแกรมกำลังทำงาน");

def get_chrome():
    custom_sleep(2);
    ky.press_and_release('ctrl+t')
    controller = keyboard.Controller();
    def enter(k):
        for i in range(k):
            if(status_run_program):# หยุดทำงาน
                print(lineNotify("\nLazada: Stop"));
                return
            controller.press(keyboard.Key.enter);
            controller.release(keyboard.Key.enter);
    
    type_and_enter("https://www.lazada.co.th/?dsource=share&laz_share_info=899993860_1_9300_100642496081_899993860_null&laz_token=164424db0b6be8cb2be84b3957c98e45&trafficFrom=17449020_303586&laz_trackid=2:mm_290511160_169702503_2126502503:clkgl3v531hpo8ndn2aopk&mkttid=clkgl3v531hpo8ndn2aopk");
    custom_sleep(2);
    enter(1)
    custom_sleep(2);
    # ky.press_and_release('ctrl+w')

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
    plat_1 = "/";
    if(status_run_program):# หยุดทำงาน
        print(lineNotify("\nLazada: Stop"));
        return
    # ********************************
    get_chrome();
    num1=int(data_link_for_lazada_gui[selected_value.get()]);
    for k in range(num1,len(data_link_for_lazada)):
        count = 0;
        if(status_run_program):# หยุดทำงาน
            print(lineNotify("\nLazada: Stop"));
            return
        print("====== Round [",k+1,"] Working [",data_link_for_lazada[k],"]======");
        Data = get_link();
        num2=(int(value_num2.get())-1);
        data_all = Data[data_link_for_lazada[k]]["lazada"];
        value_to_gui.set(len(data_all));
        # +++++++++++++++++++++++++++++++++++++++++++++++ Show_Status ++++++++++++++++++++++++++++++++++++
        Working.set(str(data_link_for_lazada[k])+"_"+str(value_num2.get())+"_"+str(value_num3.get()));
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        print(lineNotify('\nLazada: Working \nGroup: '+data_link_for_lazada[k]+'\nId: '+str(data_link_for_lazada[k])+"_"+str(value_num2.get())+"_"+str(value_num3.get())));
        # try:
        for i in range(num2,len(data_all)):
            
            # ********************************
            if(status_run_program):# หยุดทำงาน
                print(lineNotify("\nLazada: Stop"));
                return
            # ********************************
            file_name = num2+1;
             # +++++++++++++++++++++++++++++++++++++++++++++++ Show_Status ++++++++++++++++++++++++++++++++++++
            Working.set(str(data_link_for_lazada[k])+"_"+str(file_name)+"_"+str(value_num3.get()));
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
             # round_click = 3;
            num3=0; 
            status_count = False
            
            # main3("https:"+data_all[i],1,round_click,desk_top,1);
            # if(status_run_program):# หยุดทำงาน
            #     return
            status_lazada = False;
            round_click = 1;
            for c in range(0,4):
                # print("Main : เกิดข้อพิดพลาดกำลังค้นหาหน้าอีกครั้ง...")
                
                main3("https:"+data_all[i],1,round_click,desk_top,1);
             
                if(status_run_program):# หยุดทำงาน
                    print(lineNotify("\nLazada: Stop"));
                    return
                if(statusLinkJson()==False and round_click==2):
                    print("Main : ไม่พบไฟล์กรุณาเช็คเส้นทางดาวน์โหลดแล้วลองอีกครั้ง");
                    print(lineNotify('\nLazada: ไม่พบไฟล์กรุณาเช็คเส้นทางดาวน์โหลดแล้วลองอีกครั้ง \nGroup: '+str(data_link_for_lazada[k])+'\nId: '+str(data_link_for_lazada[k])+"_"+str(num2+1)+"_"+str(value_num3.get())+'\nLink: '+data_all[i]+"/?page=0"),notifyFile(path_project).text,lineNotify("\nLazada: Stop"));
                    return 
                status_lazada = check_data_count(path_remove);
                
                if(c==4):
                    print(lineNotify('\nLazada: ไม่มีหน้า \nGroup: '+str(data_link_for_lazada[k])+'\nId: '+str(data_link_for_lazada[k])+"_"+str(num2+1)+"_"+str(value_num3.get())+'\nLink: '+data_all[i]+"/?page=0"),notifyFile(path_project).text,lineNotify("\nLazada: Stop"));
                    return
                elif status_lazada :
                    break;
                round_click+=1;
                os.remove(path_remove);
            
            if(status_lazada==True):
                print("Main : ค้นหาหน้าสำเร็จ")
                status_count = check_data_count(path_file+data_lazada+data_lazada_xlsx);
            if(status_count==True):
                count = page();
                num3 = int(value_num3.get())-1
                if((num3+1)<=count):
                    error = 0;
                    round_click2 = 0;
                    while(num3<count):
                        data_sum=data_all[i]+"/?page="+str(num3+1);
                        if(error == 4):
                            print(lineNotify('\nLazad: Error \nGroup: '+str(data_link_for_lazada[k])+'\nId: '+str(data_link_for_lazada[k])+"_"+str(num2+1)+"_"+str(num3)+'\nLink: '+data_sum),notifyFile(path_project).text,lineNotify("\nLazada: Stop"));
                            log.addLog("%s_%d_%d False"%(data_link_for_lazada[k],file_name,num3))
                            print("%s_%d_%d Flase"%(data_link_for_lazada[k],file_name,num3));
                            destination_path = path_file+un_process;
                            shutil.move(path_file+path, destination_path)
                            return;
                        # ********************************
                        if(status_run_program):# หยุดทำงาน
                            print(lineNotify("\nLazada: Stop"));
                            return
                        # ********************************
                        # +++++++++++++++++++++++++++++++++++++++++++++++ Show_Status ++++++++++++++++++++++++++++++++++++
                        Working.set(str(data_link_for_lazada[k])+"_"+str(file_name)+"_"+str(num3+1));
                        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                        print("=======================");
                        print(round_click2);
                        main(data_sum,1,round_click2,desk_top,1);
                        round_click2+=1;
                        find_shopee = statusLinkJson();
                        if(find_shopee==True):
                            path = change_name(k+1,file_name,num3+1);
                            if(check_data(path_file+path)==True):
                                status_api = data_process(path_file+path,k+1,file_name,num3+1,data_link_for_lazada[k],data_sum);
                                if(status_api==False):
                                    print(lineNotify("\nLazada_Api : ไม่สามารถส่งข้อมูลได้กรุณาลองอีกครั้ง"))
                                    return
                                error = 0;
                                round_click2 = round_click2-1;
                                # ***************************************************การเพิ่1ม log ยังไม่สำเร็จ *************************
                                print("%s_%d_%d True"%(data_link_for_lazada[k],file_name,num3+1));
                                log.addLog("%s_%d_%d True"%(data_link_for_lazada[k],file_name,num3+1))
                                setTreeCommand()
                                # ***************************************************การเพิ่ม log ยังไม่สำเร็จ *************************
                                num3+=1;
                            else:
                                error+=1;
                                if(error==1 and round_click2-1>0):
                                    round_click2=0;
                                
                                continue
                        else:
                            continue;
                        print("=======================");
                        
                    
                    print(lineNotify('\nLazada: Success Id \nGroup: '+str(data_link_for_lazada[k])+'\nId: '+str(data_link_for_lazada[k])+"_"+str(num2+1)+"_"+str(num3)))
                    value_num3.set(1);
                    num2+=1;
                else:
                    print(lineNotify('\nLazad: ไม่มีหน้านี้ในเว็บกรุณาลองเลือกไหม่อีกครั้ง \nGroup: '+str(data_link_for_lazada[k])+'\nId: '+str(data_link_for_lazada[k])+"_"+str(value_num2.get())+"_"+str(num3)+'\nLink: '+data_sum),notifyFile(path_project).text,lineNotify("\nLazada: Stop"));
                    print("Main : ไม่มีหน้านี้ในเว็บกรุณาลองอีกครั้ง")
                    return;
                
                if(num2!=len(data_all) and num1<len(options)):
                    print(lineNotify('\nLazada: Next Id \nGroup: '+str(data_link_for_lazada[num1])+'\nId: '+str(data_link_for_lazada[num1])+"_"+str(num2+1)+"_"+str(value_num3.get())))
                    continue;
            else:
                print(lineNotify('\nLazad: ไม่มีหน้า \nGroup: '+str(data_link_for_lazada[k])+'\nId: '+str(data_link_for_lazada[k])+"_"+str(value_num2.get())+"_"+str(num3)+'\nLink: '+data_sum),notifyFile(path_project).text,lineNotify("\nLazada: Stop"));
                print("Main : ไม่มีหน้า")
                return;      
        # print(lineNotify('\nLazada: Success Group \nGroup:'+str(data_link_for_lazada[k])+'\nId: '+str(data_link_for_lazada[k])+"_"+str(num2+1)+"_"+str(num3)))
        num1+=1;
        value_num2.set(1)
        if(num1<len(options)):
            print(lineNotify('\nLazada: Next Group \nGroup:'+str(data_link_for_lazada[num1])+'\nId: '+str(data_link_for_lazada[num1])+"_"+str(value_num2.get())+"_"+str(value_num3.get())))
        # except Exception as e:
        #     print("For_i : ",e)
    # print(lineNotify('Bot lazada : ทำงานทุกลิงค์ครบแล้ว '));
# +++++++++++++++++++++++++++++++++++++++++++++++ Command GUI button ++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++ Command GUI button ++++++++++++++++++++++++++++++++++++
def run_system():
    global status_run_program
    status_run_program = False
    showStatusBot.set("สถาณะการทำงาน : กำลังทำงาน")
    setTreeCommand()
    t = threading.Thread(target=run)
    t.start()

def stop_program():
    global status_run_program
    status_run_program = True
    showStatusBot.set("สถาณะการทำงาน : หยุดทำงาน")
    messagebox.showinfo("โปรแกรม'หยุดทำงาน'", f"โปรแกรม'หยุดทำงาน'")

# ****************** button start and stop ***********************************************************

buttom_start = Button(app, text="start bot", bg="#9ADE7B", fg="white", command=run_system)
buttom_stop = Button(app, text="stop bot", bg="#7360DF", fg="white", command=stop_program)
buttom_clear = Button(app, text="ลบประวัติทั้งหมด", bg="#FF6868", fg="white", command=log.clearLog)

# ****************** variable ***********************************************************

value_link = get_link()
selected_value_num_2 = StringVar()
selected_value_num_3 = StringVar()
value_num2 = StringVar()
value_num2.set(1)
check_count_gui = StringVar()
check_count_gui.set(0)
value_num3 = StringVar()
value_num3.set(1)
Working = StringVar()
selected_value.set('สุขภาพและความงาม')

# ****************** แสดง log ***********************************************************

def setTreeCommand():
    table.delete(*table.get_children())
    data = log.getLog()
    for i in range(len(data) - 1, -1, -1):
        table.insert('', 'end', values=(i, data[i]))

header_gui = ['loop', 'group system']
hdsize = [50, 400]
table = ttk.Treeview(app, columns=header_gui, show='headings')

# header
for h, s in zip(header_gui, hdsize):
    table.heading(h, text=h)
    table.column(h, width=s)
setTreeCommand()

# ************************* Function *************************

def Set_value_Working():
    Working.set(str(selected_value.get()) + "_" + str(value_num2.get()) + "_" + str(value_num3.get()))

def on_dropdown_change(event):
    selected_value.set(event.widget.get())
    value_num2.set(1)
    value_num3.set(1)
    Set_value_Working()
    number_dropdown_2()
    number_dropdown_3()

def on_dropdown_change_num2(event):
    selected_num2 = event.widget.get()
    value_num2.set(selected_num2)
    Set_value_Working()

def on_dropdown_change_num3(event):
    value_num3.set(event.widget.get())
    Set_value_Working()

def number_dropdown_2():
    selected = selected_value.get()
    options_2 = [str(i) for i in range(1, 1 + len(value_link[selected]['lazada']))]
    selected_value_num_2.set(options_2[0])
    dropdown_num_2['values'] = options_2

def number_dropdown_3():
    selected = selected_value.get()
    options_3 = [str(i) for i in range(1, 103)]
    selected_value_num_3.set(options_3[0])
    dropdown_num_3['values'] = options_3

def dropdown_value_num3(value):
    selected_value_num_3 = [str(i) for i in range(value)]
    dropdown_num_3 = ttk.Combobox(app, textvariable=selected_value_num_3, values=selected_value_num_3)

# *************************************************************
showStatusBot.set("สถาณะการทำงาน : ยังไม่ทำงาน")
dropdown = ttk.Combobox(app, textvariable=selected_value, values=options)
dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)

# *************************************************************
# num_2
dropdown_num_2 = ttk.Combobox(app, textvariable=selected_value_num_2)
dropdown_num_2.bind("<<ComboboxSelected>>", on_dropdown_change_num2)

# *************************************************************
# num3
dropdown_num_3 = ttk.Combobox(app, textvariable=selected_value_num_3)
dropdown_num_3.bind("<<ComboboxSelected>>", on_dropdown_change_num3)

# *************************************************************
# terminal
text = scrolledtext.ScrolledText(app, wrap=WORD, width=60, height=15)
sys.stdout = PrintRedirector(text)

# ****************** การจัดเรียงด้วย grid ***********************************************************

buttom_start.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
buttom_stop.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
buttom_clear.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
dropdown_num_2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
dropdown_num_3.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

# ตาราง log
table.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
text.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# ปรับขนาด widget ตามขนาดหน้าต่าง
app.grid_rowconfigure(3, weight=1)  # ขยาย log table
app.grid_rowconfigure(4, weight=1)  # ขยาย text area
app.grid_columnconfigure(1, weight=1)  # ขยาย dropdown และปุ่ม
app.mainloop()
