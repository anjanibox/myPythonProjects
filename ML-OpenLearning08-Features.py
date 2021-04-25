# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:28:20 2020

@author: Tomatobox
"""

import pandas as pd
import numpy as np

df1 = pd.read_csv("C:\\Tomato-BS\DevOps\\python-scripts\\fe_binning.csv")
k = df1.head()
print(k)
# Allocate happiness to bins
binned = pd.cut(df1["happiness"], bins = [0,4.5,6,10], labels = ["L","M","H"])

# Add the binned values as a new categorical feature
df1["happiness_band"] = binned

k = df1.head()
print(k)

z = df1.groupby("happiness_band").size()

print(z)