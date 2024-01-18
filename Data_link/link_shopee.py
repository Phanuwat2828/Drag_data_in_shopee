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
import pyperclip


# https://shopee.co.th/
# -cat.11044964

# https://shopee.co.th/
# -cat.11044964
# ความงามและของใช้ส่วนตัว
# กลุ่มผลิตภัณฑ์เพื่อสุขภาพ
# เสื้อผ้าแฟชั่นผู้ชาย
# เสื้อผ้าแฟชั่นผู้หญิง
# กระเป๋า
# รองเท้าผู้ชาย
# รองเท้าผู้หญิง
# เครื่องประดับ
# นาฬิกาและแว่นตา
# เครื่องใช้ในบ้าน
# สื่อบันเทิงภายในบ้าน
# 
# เครื่องใช้ไฟฟ้าภายในบ้าน
# คอมพิวเตอร์และแล็ปท็อป
# กล้องและอุปกรณ์ถ่ายภาพ
# อาหารและเครื่องดื่ม
# ของเล่น สินค้าแม่และเด็ก
# กีฬาและกิจกรรมกลางแจ้ง
# สัตว์เลี้ยง
# เกมและอุปกรณ์เสริม

data_link  = {
    "อุปกรณ์-อิเล็กทรอนิกส์":["เกมและอุปกรณ์เสริม","กล้องและอุปกรณ์ถ่ายภาพ","มือถือและอุปกรณ์เสริม"],
    "อุปกรณ์เสริม-อิเล็กทรอนิกส์":["คอมพิวเตอร์และแล็ปท็อป"],
    "ทีวีและเครื่องใช้ในบ้าน":["สื่อบันเทิงภายในบ้าน","เครื่องใช้ไฟฟ้าภายในบ้าน"],
    "สุขภาพและความงาม":["ความงามและของใช้ส่วนตัว","กลุ่มผลิตภัณฑ์เพื่อสุขภาพ"],
    "ทารกและของเล่น":["ของเล่น-สินค้าแม่และเด็ก"],
    "ของชำและสัตว์เลี้ยง":["สัตว์เลี้ยง","อาหารและเครื่องดื่ม"],
    "บ้านและไลฟ์สไตล์":["เครื่องใช้ในบ้าน","เครื่องเขียน-หนังสือ-และงานอดิเรก"],
    "แฟชั่นและเครื่องประดับผู้หญิง":["กระเป๋า","เสื้อผ้าแฟชั่นผู้หญิง","รองเท้าผู้หญิง"],
    "แฟชั่นและเครื่องประดับผู้ชาย":["เสื้อผ้าแฟชั่นผู้ชาย","รองเท้าผู้ชาย","นาฬิกาและแว่นตา"],
    "กีฬาและการเดินทาง":["กีฬาและกิจกรรมกลางแจ้ง"],
    "ยานยนต์และรถจักรยานยนต์":["ยานยนต์"],
    "เครื่อเขียนหนังสือ":["เครื่องเขียน-หนังสือ-และงานอดิเรก"]
}
def get_link(link):
            url = link;
            data_link_all=[];
            page = requests.get(url)
            data_link_all.append(url);
            soup = b(page.content,'html.parser')
            all_link = soup.find_all('a',class_ = 'grid-cell grid-cell--with-titles');
            for link in all_link:
                href = link['href']
                if href:
                    data = "https://shopee.co.th"+href+"?page=";
                    data_link_all.append(data)
            return data_link_all
def get_in_json(json_file_path):
     with open(json_file_path, 'w', encoding='utf-8') as new_json_file:
        json.dump(existing_data, new_json_file, ensure_ascii=False, indent=2)
        print(f'ข้อมูลถูกเติมลงในไฟล์ JSON ใหม่ที่ {json_file_path}') 
# เติมข้อมูลใหม่
path_here = os.getcwd();
json_file_path = path_here+'\Data_link\data_link_all.json';
print(json_file_path)
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    existing_data = json.load(json_file)
for Id in data_link:
    data_link_1 = []
    for data in data_link[Id]:
        link = "https://shopee.co.th/"+data+"-cat.11044964";
        data_link_1 +=get_link(link);
    
    existing_data[Id]["shopee"] = [] 
    get_in_json(json_file_path);
    existing_data[Id]["shopee"]=data_link_1
    get_in_json(json_file_path);
    

            