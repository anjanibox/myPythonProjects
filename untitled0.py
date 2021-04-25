# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:36:45 2020

@author: Tomatobox
"""


import pandas as pd
df = pd.read_csv("C:\\Users\\Tomatobox\\Desktop\\OpenLearning\\titanic\\train.csv")
print(df.head())

#print(df["PassengerId"].isnull().count())
#print(df['Survived'].isna().sum())
#print(df['Pclass'].isna().sum())
#print(df['Name'].isna().sum())
#print(df['Sex'].isna().sum())
#print(df['Age'].isna().sum())
#print(df['SibSp'].isna().sum())
#print(df['Parch'].isna().sum())
#print(df['Ticket'].isna().sum())
#print(df['Fare'].isna().sum())
#print(df['Cabin'].isna().sum())
#print(df['Embarked'].isnull().sum())
#print(df['Pclass'].unique())
#print(df['Pclass'].value_counts())
#print(df['Deck'].describe())
#bins = [0, 25, 50100]
#df['binned'] = pd.cut(df['Fare']    , bins)
#s = df.groupby(pd.cut(df['Fare'], bins=bins)).size()
#print (df['binned'].describe())
print(df['Cabin'].describe())