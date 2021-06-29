import pyautogui
from time import sleep
#pyperclip
#https://pyautogui.readthedocs.io/en/latest/quickstart.html
sleep(3)
# pyautogui.position()
# pyautogui.typewrite('Hello world!\n ok\n', interval=0.1)
# pyautogui.hotkey("enter")
# pyautogui.typewrite('byeeHello world', interval=0.1)
# pyautogui.hotkey("enter")
# pyautogui.hotkey("enter")
# pyautogui.hotkey("enter")
# pyautogui.hotkey("enter")
# box = pyautogui.locateOnScreen('/home/pi/home.png')
# pyautogui.moveTo(114, 82, duration=5)
# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
p = pyautogui.position()
print("got the postions")
sleep(5)
pyautogui.moveTo(p.x, p.y, duration=5)
pyautogui.click()