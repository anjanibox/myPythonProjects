# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:04:14 2020

@author: Tomatobox
"""

import pandas as pd
#import numpy as np

df2 = pd.read_csv("C:\\Tomato-BS\DevOps\\python-scripts\\fe_splitting.csv")
print(df2.head())
df2["timestamp_of_call"] = pd.to_datetime(df2["timestamp_of_call"])
df2.dtypes
df2["day"] = df2["timestamp_of_call"].dt.day
df2["month"] = df2["timestamp_of_call"].dt.month
df2["year"] = df2["timestamp_of_call"].dt.year
df2["weekday"] = df2["timestamp_of_call"].dt.weekday
df2["hour"] = df2["timestamp_of_call"].dt.hour
#print(df2["day"] )
#print(df2["month"])
#print(df2["year"])
#print(df2["weekday"])
#print(df2["hour"])
#print()

df3 = pd.read_csv("C:\\Tomato-BS\DevOps\\python-scripts\\fe_splitting.csv")
df3.head()
df3["property_type"].unique()
df3[['property_type_type', 'property_type_size']] = df3["property_type"].str.split("-",expand=True)
df3.head()
df3.isnull().mean()

df4 = pd.read_csv("C:\\Tomato-BS\DevOps\\python-scripts\\fe_one_hot.csv")
df4.head()
region_one_hot = pd.get_dummies(df4.region)
#print(region_one_hot)

df4 = df4.join(region_one_hot).drop('region', axis=1)
df4.head()
print(df4)

