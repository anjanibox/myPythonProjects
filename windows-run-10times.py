# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:31:24 2020

@author: Tomatobox
"""


import pyautogui
for i in range(10):
      pyautogui.moveRel(100, 0, duration=0.25)
      pyautogui.moveRel(0, 100, duration=0.25)
      pyautogui.moveRel(-100, 0, duration=0.25)
      pyautogui.moveRel(0, -100, duration=0.25)