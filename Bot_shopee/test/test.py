import requests,os,json,time,pandas as pd,pyautogui,shutil,pyperclip,keyboard as ky
from fnmatch import fnmatch
from pynput import keyboard,mouse
from data_address import address as ad



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

path_file = os.getcwd();


def check_data(path_file):
    try:
        check_data=[]
        df = pd.read_excel(path_file)
        print(df.columns[0])
        # is_subset = all(item in df.columns for item in header);
        # print("Check_data : พบข้อมูลทั้งหมดใน Excel ",is_subset);
        for i in range(len(header)):
            for excel in range(len(df.columns)):
                if(header[i]==df.columns[excel]):
                    check_data.append(df.columns[excel]);
        print("Check_data : ข้อมูลที่มีทั้งหมด ",e);
        return check_data; 
    except Exception as e:
        print("Check_data : ข้อมูล Excel ",e);  

print(check_data(path_file+r'/bot_shopee/Data_shopee/data_13_1_1.xlsx'));

# col-xs-2-4 href	Fd4QmV src	hxLzax	DgXDzJ	k9JZlv	OwmBnn	JVW3E2	bPcAVl	bx++ig 2	k9JZlv 2	customized-overlay-image src
