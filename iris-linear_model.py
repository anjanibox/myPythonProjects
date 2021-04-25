# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:14:52 2020

@author: Tomatobox
"""
import pandas as pd
from functions import boxPlotAll
from functions import histPlotAll
from functions import viewDecisionTree
from functions import classComparePlot
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#1. Write down the Objective
#: Use iris data to determine irish flower
#2. Load Data
dataset = pd.read_csv("C:\\Tomato-BS\\DevOps\\python-scripts\\iris_flower.csv")
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
y = dataset["Species"]
X = dataset[["Sepallength","Sepalwidth","Petallength","Petalwidth"]]
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
viewDecisionTree(model, X.columns)