# bar_path = Mouse clicked at (608, 59) with Button.left
# ขยาย Mouse clicked at (1183, 61) with Button.left

# ส่วน ขยาย Mouse clicked at (1012, 236) with Button.left
# โหลด Mouse clicked at (577, 111) with Button.left
import time;
from pynput import mouse
import pyautogui

def on_click(x, y, button, pressed):
    if pressed:
        print(f'Mouse clicked at ({x}, {y}) with {button}')

# Create a mouse listener
with mouse.Listener(on_click=on_click) as listener:
    # Keep the script running
    listener.join()

# from pynput import keyboard
# import time

# from pynput import keyboard
# import time

# def type_and_enter(text):
#     controller = keyboard.Controller()
#     controller.type(text)
#     controller.press(keyboard.Key.enter)
#     controller.release(keyboard.Key.enter)

# Example: Type the word "Automate" and press Enter
# type_and_enter("Automate")

# Add a delay to keep the program running for a while
# time.sleep(10)



