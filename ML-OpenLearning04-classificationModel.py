# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:34:24 2020

@author: Tomatobox
"""

import pandas as pd
import numpy as np

# Import the Python machine learning libraries we need
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Import some convenient functions. This can be found on the course github
from functions import histPlotAll
from functions import boxPlotAll
from functions import classComparePlot

# Load the data
dataset = pd.read_csv("C:\\Tomato-BS\DevOps\\python-scripts\\world_data_really_tiny.csv")

# Inspect first few rows
dataset.head(12)

# Inspect data shape
dataset.shape

# Inspect descriptive stats
dataset.describe()

# View univariate histgram plots
histPlotAll(dataset)

# View univariate box plots
boxPlotAll(dataset)

# View class split
classComparePlot(dataset[["happiness","lifeexp","unemployment"]], 'happiness', plotType='hist')

# Split into input and output features
y = dataset["happiness"]
X = dataset[["lifeexp","unemployment"]]

# Split into test and training sets
test_size = 0.33
seed = 7
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)

# Select algorithm
model = DecisionTreeClassifier()

# Fit model to the data
model.fit(X_train, y_train)

# Check model performance on training data
predictions = model.predict(X_train)
print(accuracy_score(y_train, predictions))

# Evaluate the model on the test data
predictions = model.predict(X_test)
print(accuracy_score(y_test, predictions))

