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
    "อุปกรณ์-อิเล็กทรอนิกส์":["เกมและอุปกรณ์เสริม-cat.11044961","กล้องและอุปกรณ์ถ่ายภาพ-cat.11044963","มือถือและอุปกรณ์เสริม-cat.11044951"],
    "อุปกรณ์เสริม-อิเล็กทรอนิกส์":["คอมพิวเตอร์และแล็ปท็อป-cat.11044958"],
    "ทีวีและเครื่องใช้ในบ้าน":["สื่อบันเทิงภายในบ้าน-cat.11044946","เครื่องใช้ไฟฟ้าภายในบ้าน-cat.11044956"],
    "สุขภาพและความงาม":["ความงามและของใช้ส่วนตัว-cat.11044959","กลุ่มผลิตภัณฑ์เพื่อสุขภาพ-cat.11044942"],
    "ทารกและของเล่น":["ของเล่น-สินค้าแม่และเด็ก-cat.11044960"],
    "ของชำและสัตว์เลี้ยง":["สัตว์เลี้ยง-cat.11044947","อาหารและเครื่องดื่ม-cat.11044943"],
    "บ้านและไลฟ์สไตล์":["เครื่องใช้ในบ้าน-cat.11044956","เครื่อเขียนหนังสือ","เครื่องเขียน-หนังสือ-และงานอดิเรก-cat.11044957"],
    "แฟชั่นและเครื่องประดับผู้หญิง":["กระเป๋า-cat.11044964","เสื้อผ้าแฟชั่นผู้หญิง-cat.11044944","รองเท้าผู้หญิง-cat.11044948"],
    "แฟชั่นและเครื่องประดับผู้ชาย":["เสื้อผ้าแฟชั่นผู้ชาย-cat.11044945","รองเท้าผู้ชาย-cat.11044949","นาฬิกาและแว่นตา-cat.11044952"],
    "กีฬาและการเดินทาง":["กีฬาและกิจกรรมกลางแจ้ง-cat.11044962"],
    "ยานยนต์และรถจักรยานยนต์":["ยานยนต์-cat.11044950"],
    "เครื่องประดับ":["เครื่องประดับ-cat.11044954"],
    "ตั๋วและบัตรกำนัน":["ตั๋วและบัตรกำนัล-cat.11044953"]
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
json_file_path = path_here+'\data_link_all.json';
print(json_file_path)
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    existing_data = json.load(json_file)
for Id in data_link:
    data_link_1 = []
    for data in data_link[Id]:
        link = "https://shopee.co.th/"+data;
        data_link_1 +=get_link(link);
    
    existing_data[Id]["shopee"] = [] 
    get_in_json(json_file_path);
    existing_data[Id]["shopee"]=data_link_1
    get_in_json(json_file_path);
    
    

            