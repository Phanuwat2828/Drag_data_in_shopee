import pyautogui
import time as t

t.sleep(4);



# รอรับคลิกแรกจากผู้ใช้
pyautogui.mouseDown()
click_position = pyautogui.position()
print("Clicked Position:", click_position)

# รอจนกว่าผู้ใช้จะคลิกอีกครั้ง
pyautogui.mouseUp()
# x=1320, y=806