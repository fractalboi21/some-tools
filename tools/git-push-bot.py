#git push automation
#this script requires root permissions.
#how to check the current window.
#pyautogui.
#learn how to create env variables and path use them.

#  with keyboard.pressed(Key.enter):
#     sleep(5)

from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
username = ""
password = ""

def hit_enter():
    sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(2)
    

sleep(5)
keyboard.type(username)
sleep(5)
hit_enter()
keyboard.type(password)
hit_enter()

print("done")