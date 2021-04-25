# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:30:17 2020

@author: Tomatobox
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Tomato-BS\DevOps\\python-scripts\\kc_house_data.csv")


df.drop(columns = ['id', 'zipcode', 'lat', 'long', 'date'], inplace = True)
df.columnsIndex(['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
                 'waterfront', 'view', 'condition', 'grade', 'sqft_above', 
                 'sqft_basement', 'yr_built', 'yr_renovated', 'sqft_living15', 
                 'sqft_lot15'])