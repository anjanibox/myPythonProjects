# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:44:09 2020

@author: Tomatobox
"""


# Core libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot

# Sklearn processing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Sklearn classification algorithms
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

# Sklearn classification model evaluation function
from sklearn.metrics import accuracy_score

# Convenience functions. This can be found on the course github
from functions import correlationMatrix
from functions import boxPlotAll
from functions import appendEqualCountsClass
from functions import viewDecisionTree
#Load Data

dataset = pd.read_csv("C:\\Tomato-BS\DevOps\\python-scripts\\world_data.csv")

#Inspect Data
print(dataset.shape)
print(dataset.dtypes)
print(dataset.isnull().mean().sort_values())

#Clean Data
dataset = dataset.drop(["murder","urbanpopulation","unemployment"], axis=1)
# Compute the mean for each feature
means = dataset.mean().to_dict()
# Impute each null with the mean of that feature
for m in means:
  dataset[m] = dataset[m].fillna(value=means[m])

#Confirm there are no nulls:
print(dataset.isnull().mean())

#Part 2: Understand the Data
#Compute Descriptive Stats

print(dataset.describe())

#Visualize
correlationMatrix(dataset)
boxPlotAll(dataset)

#Part 3: Prepare Data

dataset = appendEqualCountsClass(dataset, "lifeexp_band", "lifeexp", 3, ["L","M","H"])
dataset.lifeexp_band.value_counts()
dataset[['lifeexp','lifeexp_band']].head()

#Select Features and Split Into Input and Target Features
y = dataset["lifeexp_band"]
X = dataset[['happiness', 'income', 'sanitation', 'water', 'literacy', 'inequality', 'energy', 'childmortality', 'fertility', 'hiv', 'foodsupply', 'population']]

#Scale Features

# Rescale the data
scaler = MinMaxScaler(feature_range=(0,1))
rescaledX = scaler.fit_transform(X)

# Convert X back to a Pandas DataFrame, for convenience
X = pd.DataFrame(rescaledX, columns=X.columns)

print(X.describe())

#Part 4: Build Models
#Split Into Test and Training Sets
test_size = 0.33
seed = 1
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=test_size, random_state=seed)


# Build a decision tree model
model_dt = DecisionTreeClassifier()
model_dt.fit(X_train, Y_train)


model_lr = LogisticRegression(solver='lbfgs', multi_class='auto')
model_lr.fit(X_train, Y_train)

#Check the Models
#accuracyscore=numberofcorrectpredictionstotalnumberofpredictions
# Check the model performance with the training data
predictions_dt = model_dt.predict(X_train)
print("DecisionTreeClassifier", accuracy_score(Y_train, predictions_dt))


# Check the model performance with the training data
predictions_lr = model_lr.predict(X_train)
print("LogisticRegression", accuracy_score(Y_train, predictions_lr))

#Evaluate Models
predictions_dt = model_dt.predict(X_test)
print("DecisionTreeClassifier", accuracy_score(Y_test, predictions_dt))


predictions_lr = model_lr.predict(X_test)
print("LogisticRegression", accuracy_score(Y_test, predictions_lr))

#Decision Tree
viewDecisionTree(model_dt, X.columns)