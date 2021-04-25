# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:54:37 2020

@author: Tomatobox
"""

import pandas as pd
import numpy as np

df1 = pd.read_csv("C:\\Tomato-BS\DevOps\\python-scripts\\fe_binning.csv")
mapping = pd.read_csv("C:\\Tomato-BS\DevOps\\python-scripts\\country_region.csv")
df1 = pd.merge(df1, mapping, left_on='country', right_on='country', how="left")
print(df1.head())