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
Mobiles
Tablets
Laptops

DSLR
Mirrorless
Point & Shoot
Instant Camera
Action/Video Cameras
Drones
Security Cameras
Console Gaming
data_link  = {
    "อุปกรณ์-อิเล็กทรอนิกส์":{
        "Mobiles":["Mobiles"],
        "Tablets":["Tablets"],
        "Laptops":["Laptops","Traditional Laptops","Gaming","2-in1-laptops"]
        
        },
        
    "อุปกรณ์เสริม-อิเล็กทรอนิกส์":,
    "ทีวีและเครื่องใช้ในบ้าน":,
    "สุขภาพและความงาม":,
    "ทารกและของเล่น":,
    "ของชำและสัตว์เลี้ยง":,
    "บ้านและไลฟ์สไตล์":,
    "แฟชั่นและเครื่องประดับผู้หญิง":,
    "แฟชั่นและเครื่องประดับผู้ชาย":,
    "กีฬาและการเดินทาง":,
    "ยานยนต์และรถจักรยานยนต์":,
    "เครื่อเขียนหนังสือ":
}
path_here = os.getcwd();
json_file_path = path_here+'\Data_link\Data_link.json'
def get_link():
    with open(json_file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
    return data;

data = get_link();

data_all = [];


for data_1 in data['datalink']:
    data_all.append(data_1.replace("https:////www.lazada.co.th/"));

print(data_all)