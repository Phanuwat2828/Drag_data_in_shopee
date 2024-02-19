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
from data_address import address as ad

uri_API = ""



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
    # try:
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
            print(read_excel[header[j]][i],j);
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
        sold = (Product[data]["sold"].split(" ")[0]=="nan")and "0" or type(Product[data]["sold"].split(" ")[0] )
        address = (Product[data]["place"]=='nan')and "" or ad[Product[data]["place"]]
        count_review = (Product[data]["count_review"]=="nan")and "0" or Product[data]["count_review"]
        maket = Product[data]["maket"]
        # ****************************************************************
        success_data_text += f'APRODUCT:::maket:::{maket}, group:::{group}, product:::{product}, price_product_2:::{""}, price_product_1:::{price_product}, image_product_1:::{image_product_1}, discount:::{discount}, image_product_2:::{image_product_2}, data_product:::{data_product}, price_before:::{""}, Emoji:::{""}, sold:::{sold}, place:::{address}, Recommended_shops:::{""}, count_review:::{count_review}'
        # ถ้าข้อมูลครบ 60 ค่อยบันทึก .json และส่ง API
        if(i==num_rows-1):
            print(success_data_text)
            print(postAPI_DB(success_data_text,id_shop,group,link));

bot_lazada = r'\Bot_lazada'
path_file = os.getcwd();
drag_data = os.path.abspath(os.path.join(path_file, os.pardir))
data_lazada = r'\Data_lazada';
data_lazada_xlsx = r'\lazada.xlsx';
un_process = r'\Unprocess';
data_link = r'\Data_link\data_link_all.json';
# ชื่อ xlsx
xlsx_test = r'\data_0_1_1.xlsx';
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
data_process(path_file+data_lazada+xlsx_test,1,1,1,'อุปกรณ์-อิเล็กทรอนิกส์',"")
