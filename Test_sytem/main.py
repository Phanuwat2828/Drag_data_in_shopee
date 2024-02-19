# bar_path = Mouse clicked at (608, 59) with Button.left
# bar_path = Mouse clicked at (608, 59) with Button.left
# ขยาย Mouse clicked at (1183, 61) with Button.left # Mouse clicked at (1222, 61) with Button.left
# reset Mouse clicked at (100, 60) with Button.left

# ส่วน ขยาย Mouse clicked at (1012, 236) with Button.left
# โหลด Mouse clicked at (577, 111) with Button.left
# Mouse clicked at (992, 291) with Button.left
import time;
from pynput import mouse
import pyautogui
from pynput import keyboard
import os
import shutil
Data = ['https://shopee.co.th/%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%87%E0%B8%B2%E0%B8%A1%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%AA%E0%B9%88%E0%B8%A7%E0%B8%99%E0%B8%95%E0%B8%B1%E0%B8%A7-cat.11044959?page=',
        
        ]


def custom_sleep(seconds):
    time.sleep(seconds)
def Scoll():
    custom_sleep(2);
    pyautogui.scroll(-2000);
    custom_sleep(6);
    pyautogui.scroll(-2000);
    custom_sleep(6)
    pyautogui.scroll(-2000);
    custom_sleep(6);
    pyautogui.scroll(-800);
    custom_sleep(6);
def click(x,y):
    pyautogui.click(x,y);
    custom_sleep(1.5);

def type_and_enter(text):
    controller = keyboard.Controller()
    controller.type(text)
    custom_sleep(2);
    controller.press(keyboard.Key.enter)
    controller.release(keyboard.Key.enter)

def main(x):
      # path
    custom_sleep(3);
    click(373, 62);
    # input path
    type_and_enter(x);
    custom_sleep(4);
    # Mouse clicked at (1360, 264) with Button.left
    custom_sleep(1);
    click(1257, 191);

    Scoll();
    # เลือกส่วนขยาย
    click(1183, 61)
    # ส่วนขยาย sracper
    click(1012,236);
    # download
    custom_sleep(2);
    click(721, 192);
    # reface
    click(100,60);
def changdeta_and_changename(i,j):
        # ระบุที่อยู่ของไฟล์และโฟลเดอร์ใหม่
    current_directory = r'C:\Users\\naken\Downloads'
    current_file_name = 'shopee.xlsx'
    new_directory = r'C:\Data_shopee'
    new_file_name = 'data_'+str(i)+'_'+str(j)+'.xlsx'

    # สร้างโฟลเดอร์ใหม่ถ้ายังไม่มี
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    # สร้างที่อยู่เต็มของไฟล์ปัจจุบันและไฟล์ใหม่
    current_file_path = os.path.join(current_directory, current_file_name)
    new_file_path = os.path.join(new_directory, new_file_name)

    # ย้าย (เปลี่ยนชื่อ) ไฟล์ไปยังโฟลเดอร์ใหม่
    shutil.move(current_file_path, new_file_path)
    


if __name__ == "__main__":
    
    num2=1;
    for i in range(len(Data)):
        num1=0;
        for j in range(9):
            data_sum=Data[i]+str(num1);
            main(data_sum);
            num1+=1;
            changdeta_and_changename(num2,num1);
        num2+=1;
    
# Mouse clicked at (1222, 61) with Button.left
# Mouse clicked at (721, 192) with Button.left
