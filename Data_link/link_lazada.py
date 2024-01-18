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