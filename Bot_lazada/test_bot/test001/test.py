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


path_file = os.getcwd();
drag_data = os.path.abspath(os.path.join(path_file, os.pardir))
data_lazada = r'\Data_lazada';
data_lazada_xlsx = r'\lazada.xlsx';
un_process = r'\Unprocess';
data_link = r'\Data_link\data_link_all.json';
test = r'\data_1_1_1.xlsx'

def check_data(path_file):
    try:
        header = ['_95X4G href', 'jBwCF src', 'jBwCF src 2'
          , 'RfADt', 'ooOxS',
       '_1cEkb', 'qzqFw', 'oa6ri']
       
        df = pd.read_excel(path_file)
        is_subset = all(item in df.columns for item in header);
        print("Check_data : ",is_subset);
        return is_subset; 
    except Exception as e:
        print("Check_data : ",e);  
check_data(path_file+data_lazada+test);
# 
# c:\Drag_data_in_shopee\Bot_lazada>python -u 
# "c:\Drag_data_in_shopee\Bot_lazada\main_lazada.py"
# Del_file : True
# ====== Round [ 1 ] Working ======
# Get_link : True
# Main : True
# Status :  True
# Status Check_Data_count :  True
# page_count :  102      
# =======================
# Main : True
# Status :  True
# Change_name :  \Data_lazada\data_1_1_1.xlsx
# Check_data :  False
# For_j Destination path 'c:\Drag_data_in_shopee\Bot_lazada\Unprocess\data_1_1_1.xlsx' already exists
# For_i : True




