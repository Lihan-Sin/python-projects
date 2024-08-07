import pyautogui
import time
message = 1 
while message <=10:
    time.sleep(0)
    pyautogui.typewrite("!!HAPPY BIRTHDAY!!"+str( message))
    pyautogui.press("enter")
    time.sleep(0)
    message = message + 1
