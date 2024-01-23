import requests
from bs4 import BeautifulSoup as b
import os
from fnmatch import fnmatch
import pandas as pd
import json
import time;
from pynput import mouse
import pyautogui
from pynput import keyboard
import shutil
import keyboard as ky
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip

# path
bot_lazada = r'\Bot_lazada'
path_file = os.getcwd();
drag_data = os.path.abspath(os.path.join(path_file, os.pardir))
data_lazada = r'\Data_lazada';
data_lazada_xlsx = r'\lazada.xlsx';
un_process = r'\Unprocess';
data_link = r'\Data_link\data_link_all.json';
desk_top = 6;
# link_json
data_link_for_lazada  = {
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
    10: 'ยานยนต์และรถจักรยานยนต์'}
# head_excel
header = ['_95X4G href', 'jBwCF src', 'jBwCF src 2'
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
# Data_Link
# Link_all
# Find_file_Donwload_after_change_name
def status():
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
            status=file_name==file;
        print("Status : ",status)
        return status;
    except Exception as e:
        print("Status : ",e);
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
        header = ['_95X4G href', 'jBwCF src', 'jBwCF src 2'
          , 'RfADt', 'ooOxS', 'oa6ri']
       
        df = pd.read_excel(path_file)
        is_subset = all(item in df.columns for item in header);
        print("Check_data : ",is_subset);
        return is_subset; 
    except Exception as e:
        print("Check_data : ",e);  


# Read Excell
# https://11c2-14-207-200-101.ngrok-free.app/


def data_process(path_file,i1,i2,i3,group):
    """
    Process : เพื่อจัดตำแหน่งข้อมูลให้สามารถป้อนเข้า Data Base ได้

    Args:
        path_file (_type_): _description_
        i1 (_type_): _description_
        i2 (_type_): _description_
        i3 (_type_): _description_
        group (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        def postAPI_DB(data,id_shop,groub,i1):
            try:
                response = requests.post(
                    f"https://bf25-202-28-35-197.ngrok-free.app/addb?id={id_shop}&&web=lazada&&group={i1}&&title_group={groub}",
                    headers={
                        "Content-type":"application/x-www-form-urlencoded"
                    },
                    data={
                        "data":data
                    }
                )
            except:
                response = "API error"
            return response
        # path_file = './Data_shopee/Data_1_1_1.xlsx';
        find = pd.read_excel(path_file);
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
            for j in range(len(header)):
                data_input = str(find[header[j]][i]);
                data_process[header_Values[header[j]]]=data_input;
            Product[data]=data_process;
            Product[data]["maket"]="lazada";
            Product[data]["group"]=group;
            # id_shop = f"shop"+str(i1)+"_"+str(i2)+"_"+str(i3);
            id_shop = f'shop{i1}_{i2}_{i3}';
            product = Product[data]["product"]
            image_product_1 = Product[data]["image_product_1"]
            image_product_2 = Product[data]["image_product_2"]
            discount = Product[data]["discount"]
            data_product = Product[data]["data_product"]
            price_product = float(Product[data]["price_product"].replace("฿","").replace(",",""))
            sold = Product[data]["sold"].split(" ")[0];
            address = Product[data]["place"]
            count_review = Product[data]["count_review"];
            group_1 = Product[data]["group"],
            maket = Product[data]["maket"];
            # ****************************************************************
            success_data_text += f'APRODUCT:::maket:::{maket}, group:::{group}, product:::{product}, price_product_2:::{""}, price_product_1:::{price_product}, image_product_1:::{image_product_1}, discount:::{discount}, image_product_2:::{image_product_2}, data_product:::{data_product}, price_before:::{""}, Emoji:::{""}, sold:::{sold}, place:::{address}, Recommended_shops:::{""}, count_review:::{count_review}'
            data_all.append(Product);
            success_data = {
                "group":i1,
                "id":id_shop,
                "title_Grop":group,
                "website":"lazada",
                "data":data_all,
                 
            }
            # ถ้าข้อมูลครบ 60 ค่อยบันทึก .json และส่ง API
            if(i==num_rows-1):
                filename = "Data_process.json"
                with open(filename, 'w', encoding='utf-8') as file:
                    json.dump(success_data, file, indent=2, ensure_ascii=False)
                test = len(Data_everthing);
                # แสดงข้อมูล
                # print(success_data_text); #ข้อมูลที่จะส่งไป API
                print(postAPI_DB(success_data_text,id_shop,group,i1));
        print("data_process : True")
    except Exception as e:
        print("data_process : ",e)

# Check_count
def check_data_count(path):
    try:
        header = ['ant-pagination-item 6']
        df = pd.read_excel(path)
        is_subset = all(item in df.columns for item in header);
        print("Status Check_Data_count : ",is_subset);
        return is_subset;
    except Exception as e:
        print("Status Check_Data_count : ",e);
def page():
    try:
        path = path_file+data_lazada+data_lazada_xlsx
        df = pd.read_excel(path)
        test ='ant-pagination-item 6'
        num = [];
        num.append(int(df[test][2]))
        os.remove(path);
        print("page_count : ",num[0]);
        return num[0];
    except Exception as e:
        print("page_count : ",e);


def Del():
    folder_path = path_file+data_lazada;
    # ลบไฟล์ทั้งหมดในโฟลเดอร์
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            print("Del_file : True")
        except Exception as e:
            print(f"Del_file : False",e);
Del();
Data = [];



def custom_sleep(seconds):
    time.sleep(seconds)
def Scoll():
    custom_sleep(2);
    for i in range(7):
        pyautogui.scroll(-750);
        custom_sleep(6);
def click(x,y):
    pyautogui.click(x,y);
    custom_sleep(1.5);
def type_and_enter(text):
    controller = keyboard.Controller();
    # controller.type(text);
    pyperclip.copy(text)
    ky.press_and_release('ctrl+v')
    custom_sleep(1);
    
def main(x,t,e,t2,e2):
    controller = keyboard.Controller();
    custom_sleep(3);
    ky.press_and_release('ctrl+t')
    def enter(k):
        for i in range(k):
            controller.press(keyboard.Key.enter);
            controller.release(keyboard.Key.enter);
    def tab(t):
        for i in range(t):
            controller.press(keyboard.Key.tab);
            controller.release(keyboard.Key.tab);
    # input path
    type_and_enter(x);
    custom_sleep(2);
    enter(1)
    # Mouse clicked at (1360, 264) with Button.left
    custom_sleep(4);
    tab(1)
    Scoll();
    ky.press_and_release('ctrl+m');

    custom_sleep(4);
    # Mouse clicked at (834, 114) with Button.left
    # Mouse clicked at (755, 179) with Button.left
# Mouse clicked at (1006, 88) with Button.left
    ky.press_and_release('F11')
    custom_sleep(4);
    tab(t);
    custom_sleep(4);
    enter(e)
    custom_sleep(1);
    tab(t2);
    custom_sleep(1);
    enter(e2)
    # Mouse clicked at (1118, 17) with Button.left
    custom_sleep(2);
    ky.press_and_release('alt+F4')
    # reface
    custom_sleep(1);
    ky.press_and_release('ctrl+w')
    print("Main : True");


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
        print("Change_name : ",path)
        return path;
    except Exception as e:
        print("Change_name : ",e)


# Link_from_json
def get_link():
    try:
        path_here = os.getcwd();
        path_here = os.path.abspath(os.path.join(path_here, os.pardir))
        path = drag_data+data_link;
        with open(path, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
        print("Get_link : True")
        return data;
    except Exception as e:
        print("Get_link : ",e);
if __name__ == "__main__":
    num1=0
    for k in range(len(data_link_for_lazada)):
        print("====== Round [",k+1,"] Working ======")
        num1+=1;
        Data = get_link();
        num2=0;
        data_all = Data[data_link_for_lazada[k]]["lazada"];
        try:
            for i in range(len(data_all)):
                num2+=1;
                num3=0; 
                status_count = False
                main(data_all[i],1,2,desk_top,1);
                status_lazada = status();
                for c in range(status_lazada==False):
                    main(data_all[i],1,2,desk_top,1);
                    if(c==2):
                        break;
                try:
                    if(status_lazada==True):
                        status_count = check_data_count(path_file+data_lazada+data_lazada_xlsx)
                    if(status_count==True):
                        count = page()
                        for j in range(count):
                            print("=======================");
                            data_sum=data_all[i]+"/?page="+str(j+1);
                            main(data_sum,desk_top+1,1,0,0);
                            find_shopee = status();
                            if(find_shopee==True):
                                num3+=1;
                                path = change_name(num1,num2,num3);

                                if(check_data(path_file+path)==True):
                                    data_process(path_file+path,num1,num2,num3,data_link_for_lazada[k]);
                                else:
                                    destination_path = path_file+un_process;
                                    shutil.move(path_file+path, destination_path)
                                    continue;
                            else:
                                continue;
                            print("=======================");
                        custom_sleep(120);
                    else:
                        continue;
                    print("For_J : True");
                except Exception as e:
                    print("For_j",e);
                print("For_i : True");
        except Exception as e:
            print("For_i : ",e);
        
