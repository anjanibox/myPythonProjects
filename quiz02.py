# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:39:22 2020

@author: Tomatobox
"""


import pandas as pd
df = pd.read_csv("C:\\Tomato-BS\DevOps\\python-scripts\\titanic.csv")
#print(df)
df.describe()
##print(df.describe())
##print(df.isnull().mean())
#print(df.Pclass.unique())
#print(df.Pclass.value_counts())

k = df.Fare.describe()
#   print(k)

# Allocate Fare to bins. 
binned = pd.cut(df["Fare"], bins = [0,7.910400,14.454200,31.000000,512.329200], labels = ["Q1","Q2","Q3","Q4"], include_lowest=True)

# Add the binned values as a new categorical feature
df["fare_band"] = binned
df.groupby("fare_band")["Fare"].min()
df.groupby("fare_band")["Fare"].max()

df["Deck"]  = df["Cabin"].str[0]

df.Deck.value_counts()

