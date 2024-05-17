import pyautogui
import threading

# กำหนดฟังก์ชันสำหรับการคลิก
def click():
    while True:
        # ย้ายตำแหน่ง cursor ไปยังตำแหน่งที่ต่ำที่สุด (x, y)
        pyautogui.moveTo(1320,806)
        pyautogui.click()

# เริ่มสร้าง thread สำหรับการคลิก
click_thread = threading.Thread(target=click)
click_thread.start()

# ลูปสำหรับการรับคำสั่งจากผู้ใช้
while True:
    command = input("Press 't' to stop clicking, 's' to start clicking Python: ")
    if command.lower() == 't':
        click_thread.join()  # หยุด thread ที่คลิก
    elif command.lower() == 's':
        click_thread = threading.Thread(target=click)
        click_thread.start()
    else:
        print("Invalid command. Please press 't' or 's'.")