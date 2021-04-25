# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:32:16 2020

@author: Tomatobox
"""
import pyautogui
from datetime import date
from datetime import datetime

print('Press Ctrl-C to quit.')
try:
 while True:
  pyautogui.moveRel(100, 20, duration=0.25)
  pyautogui.click(100, 20)
  pyautogui.moveRel(20, 100, duration=0.25)
  pyautogui.click(20, 100)
  pyautogui.moveRel(-100, 20, duration=0.25)
  pyautogui.click(-100, 20)
  pyautogui.moveRel(20, -100, duration=0.25)
  pyautogui.click(20, -100)
  today = date.today()
  now = datetime.now()
  d4 = today.strftime("%b-%d-%Y")
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  print(d4 + " " +dt_string)
except KeyboardInterrupt:
  print('\nDone.')  