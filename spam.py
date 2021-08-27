
#import relevant module

import time
import pyautogui


def sendspam():


 time.sleep(5)
text = open('spam.txt')
for each_line in text:
    pyautogui.typewrite(each_line)
    pyautogui.press('enter')
sendspam()








