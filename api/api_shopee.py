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
import test_api_ as api


header = ['col-xs-2-4 href', 'Fd4QmV src', 'FTxtVW',
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
def data_process(path_file,i1,i2,i3,group):
    try:
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
            # ***************************ไอดีสินค้าหลัก*************************************
            id_shop = "shop"+str(i1)+"_"+str(i2)+"_"+str(i3);
            # ****************************************************************
            success_data_text += f'APRODUCT:::maket:::{Product[data]["maket"]}, group:::{group}, product:::{Product[data]["product"]}, price_product_2:::{float(Product[data]["price_product_2"].replace(",",""))}, price_product_1:::{float(Product[data]["price_product_1"].replace(",",""))}, image_product_1:::{Product[data]["image_product_1"]}, discount:::{Product[data]["discount"]}, image_product_2:::{Product[data]["image_product_2"]}, data_product:::{Product[data]["data_product"]}, price_before:::{Product[data]["price_before"]}, Emoji:::{Product[data]["Emoji"]}, sold:::{Product[data]["sold"]}, place:::{Product[data]["place"]}, Recommended_shops:::{Product[data]["Recommended_shops"]}'
            data_all.append(Product);
            success_data = {
                 "id":id_shop,
                 "data":data_all
            }
            # ถ้าข้อมูลครบ 60 ค่อยบันทึก .json และส่ง API
            if(i==num_rows-1):
                filename = "Data_process.json"
                with open(filename, 'w', encoding='utf-8') as file:
                    json.dump(success_data, file, indent=2, ensure_ascii=False)
                test = len(Data_everthing);
                # แสดงข้อมูล
                # print(success_data_text); #ข้อมูลที่จะส่งไป API
                print(api.postAPI_DB(success_data_text,id_shop));
        print("data_process : True")
    except Exception as e:
        print("data_process : ",e)