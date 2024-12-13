# -*- coding: utf-8 -*-
"""Iris dataset

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1orxG0YMoENUSrSahTe6Hg9GqSWJfICOz
"""

# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
iris_data = pd.DataFrame(iris.data, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
iris_data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Splitting the dataset into features (X) and target (y)
X = iris_data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = iris_data["species"]

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

# Displaying results
print("Sample Data:")
print(iris_data.head())
print("\nModel Accuracy:", accuracy)
print("\nClassification Report:\n", report)