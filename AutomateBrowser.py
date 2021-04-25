# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:23:29 2020

@author: Tomatobox
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
try:
 while True:
     url = "https://localhost/DOC-1657229" #Top tools
     fp = webdriver.FirefoxProfile('C:\\Users\\Tomatobox\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ysuexwta.Default User')
    driver = webdriver.Firefox(executable_path='C:\\Tomato-BS\\DevOps\\python-scripts\\geckodriver.exe', firefox_profile=fp)
     delay = 3 # seconds
     timeout = 5

     try:
          driver.get(url)
          element_present = EC.presence_of_element_located((By.ID, 'top'))
          WebDriverWait(driver, timeout).until(element_present)
          driver.close()
          driver.quit()
          print ("Loading completed!")
     except TimeoutException:
        print ("Loading took too much time!")
except KeyboardInterrupt:
  print('\nDone.')  