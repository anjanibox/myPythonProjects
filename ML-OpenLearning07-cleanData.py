# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:58:00 2020

@author: Tomatobox
"""

import pandas as pd
import numpy as np

#Load Data

dataset = pd.read_csv("C:\\Tomato-BS\DevOps\\python-scripts\\CleanYourData.csv")
df = dataset
#print(dataset)
#print(dataset.describe())
#df["date_of_sale"] = pd.to_datetime(df["date_of_sale"])
#df['number_of_bedrooms'] = pd.to_numeric(df['number_of_bedrooms'])
#df['price'] = pd.to_numeric(df['price'])
##df.loc[7,'number_of_bedrooms'] = np.NaN
##df = df.dropna(axis=1)
#print(df)
#print(df["date_of_sale"])
#print(df['number_of_bedrooms'])
#print(df['price'])
#print(non_nums)
#print(df['type'])

#Convert data types
non_nums = df[~df["number_of_bedrooms"].str.isnumeric()]["number_of_bedrooms"].unique()

#Replace values
df["number_of_bedrooms"] = df["number_of_bedrooms"].replace(non_nums, np.nan)
df["type"] = df["type"].replace(['teraced'], 'terraced')



#Remove outliers
df["price"] = df["price"].apply(lambda x: x.replace('£', '') if type(x) is str else x)
df["price"] = df["price"].apply(lambda x: x.replace(',', '') if type(x) is str else x)
df['price'] = pd.to_numeric(df['price'])
mean = df["price"].mean()    
df["price"] = df["price"].fillna(value=mean) 


#Replace outlier values

#Remove duplicates
df = df.drop_duplicates()

#Remove columns containing nulls
#df.groupby('location')['number_of_bedrooms'].transform(lambda x: x.fillna(x.mean()))



#Remove rows containing nulls
df = df.dropna()

#Impute nulls with the mean or median

#Impute nulls with the group mean or median
    
#print(df['price'])
print(df)

# Extract the year
#df['year'] = df[]

# Impute null prices with the mean for the location, bedrooms and year of sale
#df.groupby(['location','number_of_bedrooms','year'])['price'].transform(lambda x: x.fillna(x.mean()))