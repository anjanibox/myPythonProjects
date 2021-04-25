# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 08:46:21 2020

@author: Tomatobox
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
# Import the Python machine learning libraries we need
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
from sklearn.metrics import accuracy_score
import sklearn.tree as tree
import pydotplus
from sklearn.externals.six import StringIO 
from IPython.display import Image

from functions import boxPlotAll
from functions import histPlotAll
from functions import viewDecisionTree
from functions import classComparePlot


#1. Write down the Objective
#: Use life expectancy and long-term unemployment rate to predict the perceived happiness (low or high) of inhabitants of a country.
#2. Load Data
dataset = pd.read_csv("C:\\Tomato-BS\\DevOps\\python-scripts\\world_data_really_tiny.csv")
#3. Inspect the data;
print(dataset.head(12))
print(dataset.describe())
#4. Visualize
histPlotAll(dataset)
boxPlotAll(dataset)
#5. Select features; 
#We can select happiness as the feature to predict (y) and lifeexp and unemployment as the features to make the prediction (X):
#6. Split into input and traget Features
# Split into input and output features
y = dataset["happiness"]
X = dataset[["lifeexp","unemployment"]]
print(X.head())
print(y.head())
#7. Split into Training and Test Sets
test_size = 0.33
seed = 7
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)
print("X train \n", X_train)
print("y train \n" , y_train)
print("y test \n" , y_test)
#8. ,  Algorithms
# Select algorithm
model = DecisionTreeClassifier()
#model = LogisticRegression(solver='lbfgs', multi_class='auto')
#model = linear_model.LinearRegression()

#9. Fit Model
# Fit model to the data
model.fit(X_train, y_train)

#10. Check Model
# Check model performance on training data
predictions = model.predict(X_train)
print(accuracy_score(y_train, predictions))
#11. Compute Accuracy Score

# Evaluate the model on the test data
predictions = model.predict(X_test)
print(accuracy_score(y_test, predictions))