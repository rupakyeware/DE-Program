# -*- coding: utf-8 -*-
"""DE7-8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-hBRyNMhAirTNyD-OVSY4tVAZ-dPXotW
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load the IRIS Dataset
data = load_iris()
print(data)
X = pd.DataFrame(data['data'], columns=data['feature_names'])
y = pd.Series(data['target'], name='target')

# Show the first few rows of the dataset
print("Features (X):")
print(X.head())
print("\nTarget (y):")
print(y.head())

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"Training set size: {X_train.shape}")
print(f"Testing set size: {X_test.shape}")

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Show a preview of the scaled data
print("First 5 rows of the scaled training data:")
print(pd.DataFrame(X_train, columns=data['feature_names']).head())

# Model Building
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Display training completion
print("Logistic Regression model trained successfully.")

# KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)

# Display training completion
print("KNN model trained successfully.")

# Logistic Regression Prediction
y_pred_log = log_reg.predict(X_test)
print("Logistic Regression Predictions:")
print(y_pred_log[:10])  # Show first 10 predictions

# KNN Prediction
y_pred_knn = knn.predict(X_test)
print("KNN Predictions:")
print(y_pred_knn[:10])  # Show first 10 predictions

# Performance Analysis -  Logistic Regression

# Accuracy
accuracy_log = accuracy_score(y_test, y_pred_log)
print(f"Logistic Regression Accuracy: {accuracy_log}")

# Confusion Matrix
cm_log = confusion_matrix(y_test, y_pred_log)
print("Confusion Matrix (Logistic Regression):")
print(cm_log)

# Visualize Confusion Matrix
sns.heatmap(cm_log, annot=True)
plt.title('Logistic Regression Confusion Matrix')
plt.show()

# Classification Report
print("Classification Report (Logistic Regression):")
print(classification_report(y_test, y_pred_log))

# Performance Analysis -  KNN

# Accuracy
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"KNN Accuracy: {accuracy_knn}")

# Confusion Matrix
cm_knn = confusion_matrix(y_test, y_pred_knn)
print("Confusion Matrix (KNN):")
print(cm_knn)

# Visualize Confusion Matrix
sns.heatmap(cm_knn, annot=True, fmt='d')
plt.title('KNN Confusion Matrix')
plt.show()

# Classification Report
print("Classification Report (KNN):")
print(classification_report(y_test, y_pred_knn))

# Comparing and Training Multiple Classifiers

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

y_pred_dt = dt.predict(X_test)
print("Decision Tree Predictions:")
print(y_pred_dt[:10])

# Random Forest
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier() # Pass parameters
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)
print("Random Forest Predictions:")
print(y_pred_rf[:10])

# Collect accuracy scores
classifiers = ['Logistic Regression', 'KNN', 'Decision Tree', 'Random Forest']
accuracies = [
    accuracy_log,
    accuracy_knn,
    accuracy_score(y_test, y_pred_dt),
    accuracy_score(y_test, y_pred_rf)
]

# Plot the comparison
plt.bar(classifiers, accuracies)
plt.ylabel('Accuracy')
plt.title('Classifier Accuracy Comparison')
plt.show()

# Parameter Tuning
# Grid Search