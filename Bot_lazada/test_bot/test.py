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


path_file = os.getcwd();
drag_data = os.path.abspath(os.path.join(path_file, os.pardir))
data_lazada = r'\Data_lazada';
data_lazada_xlsx = r'\lazada.xlsx';
un_process = r'\Unprocess';
data_link = r'\Data_link\data_link_all.json';
test = r'\data_1_1_2.xlsx'


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if fnmatch(filename, pattern):
                status = True  
                yield os.path.join(root, filename)

def status():
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

status()

