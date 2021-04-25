# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:03:10 2020

@author: Tomatobox
"""

#Import Libraries
# Import Python libraries for data manipuation and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
# Import the Python machine learning libraries we need
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import sklearn.tree as tree
import pydotplus
from sklearn.externals.six import StringIO 
from IPython.display import Image

from functions import boxPlotAll
from functions import histPlotAll
from functions import viewDecisionTree
from functions import classComparePlot

#1. Define the Task
#Remember the task:Use life expectancy and long-term unemployment rate to predict the perceived happiness (low or high) of inhabitants of a country.

#2. Load the data set
dataset = pd.read_csv("C:\\Tomato-BS\\DevOps\\python-scripts\\world_data_really_tiny.csv")

#3. Understand the Data
#3.1 Inspect the Data
#3.1.1 Inspect first few rows
print(dataset.head(12))

#3.1.2 Inspect data shape
dataset.shape
print(dataset.shape)

#3.1.3 Inspect descriptive stats
print(dataset.describe())

#3.2 Visualize the Data
#3.2.1 View univariate histgram plots
histPlotAll(dataset)

#3.2.2 View univariate box plots
boxPlotAll(dataset)

#3.2.3 View class split
classComparePlot(dataset[["happiness","lifeexp","unemployment"]], 'happiness', plotType='hist')

#4. Prepare the Data for Supervised Machine Learning
#4.1 Select Features and Split Into Input and Target Features
y = dataset["happiness"]
X = dataset[["lifeexp","unemployment"]]
print(X.head())
print(y.head())

#5. Build a Model
#5.1 Split Into Training and Test Sets
test_size = 0.33
seed = 7
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)
print(X_train)
print(X_test)
print(y_train)

#5.2 Select an Algorithm
model = DecisionTreeClassifier()

#5.3 Fit the Model to the Data
model.fit(X_train, y_train)
#print(model.fit)

#5.4 Check the Model
predictions = model.predict(X_train)
#print(predictions)
#print(accuracy_score(y_train, predictions))

#6. Evaluate the Model
#6.1 Compute Accuracy Score
predictions = model.predict(X_test)
#print(predictions)
#print(accuracy_score(y_test, predictions))
#df = X_test.copy()
#df['Actual'] = y_test
#df['Prediction'] = predictions
print(viewDecisionTree(model, X.columns))