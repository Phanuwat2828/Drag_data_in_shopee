import os
import shutil

# ระบุที่อยู่ของไฟล์และโฟลเดอร์ใหม่
current_directory = r'C:\Users\\naken\Downloads'
current_file_name = 'shopee.xlsx'
new_directory = r'C:\Data_shopee'
new_file_name = 'data_1.xlsx'

# สร้างโฟลเดอร์ใหม่ถ้ายังไม่มี
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

# สร้างที่อยู่เต็มของไฟล์ปัจจุบันและไฟล์ใหม่
current_file_path = os.path.join(current_directory, current_file_name)
new_file_path = os.path.join(new_directory, new_file_name)

# ย้าย (เปลี่ยนชื่อ) ไฟล์ไปยังโฟลเดอร์ใหม่
shutil.move(current_file_path, new_file_path)
