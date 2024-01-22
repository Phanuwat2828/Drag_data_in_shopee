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



def data_process(path_file,i1,i2,i3,group):
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

bot_lazada = r'\Bot_lazada'
path_file = os.getcwd();
drag_data = os.path.abspath(os.path.join(path_file, os.pardir))
data_lazada = r'\Data_lazada_test_api';
data_lazada_xlsx = r'\lazada.xlsx';
un_process = r'\Unprocess';
data_link = r'\Data_link\data_link_all.json';
# ชื่อ xlsx
xlsx_test = r'\data_1_1_1.xlsx';
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

data_process(path_file+data_lazada+xlsx_test,1,1,1,'อุปกรณ์-อิเล็กทรอนิกส์')