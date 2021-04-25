# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:07:02 2020

@author: Tomatobox
"""


# Core libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sklearn processing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Sklearn regression algorithms
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

# Sklearn regression model evaluation function
from sklearn.metrics import mean_absolute_error

from functions import scatterMatrix
from functions import linearRegressionSummary
#from functions import models


#Define the Task
#Make predictions about a country's life expectancy in years from a set of metrics for the country.

#Acquire Clean Data
dataset = pd.read_csv("world_data.csv")

# Remove sparsely populated features
dataset = dataset.drop(["murder","urbanpopulation","unemployment"], axis=1)

# Impute all features with mean
means = dataset.mean().to_dict()
for m in means:
  dataset[m] = dataset[m].fillna(value=means[m])

#Understand the Data
print(plt.style.available)
['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', 'Solarize_Light2', 'tableau-colorblind10', '_classic_test']
plt.style.use('bmh')
dataset.hist(figsize=(20,20))
plt.show() 

scatterMatrix(dataset)

#Prepare Data
y = dataset["lifeexp"]
X = dataset[['happiness', 'income', 'sanitation', 'water', 'literacy', 'inequality', 'energy', 'childmortality', 'fertility', 'hiv', 'foodsupply', 'population']]


# Rescale the data
scaler = MinMaxScaler(feature_range=(0,1))
rescaledX = scaler.fit_transform(X)

# Convert X back to a Pandas DataFrame, for convenience
X = pd.DataFrame(rescaledX, index=X.index, columns=X.columns)

#Build Models

#Split Into Test and Training Sets
test_size = 0.33
seed = 1
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=test_size, random_state=seed)

#Create Multiple Models, Fit and Check Them
models = [LinearRegression(), KNeighborsRegressor()]

for model in models:
  model.fit(X_train, Y_train)
  predictions = model.predict(X_train)
  print(type(model).__name__, mean_absolute_error(Y_train, predictions))

#Evaluate Models
for model in models:
  predictions = model.predict(X_test)
  print(type(model).__name__, mean_absolute_error(Y_test, predictions))
  
#print(linearRegressionSummary(model,X_test))