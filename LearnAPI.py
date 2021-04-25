# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:25:18 2021

@author: Tomatobox
"""
import requests
response = requests.get("https://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())