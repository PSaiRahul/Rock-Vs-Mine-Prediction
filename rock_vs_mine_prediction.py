# -*- coding: utf-8 -*-
"""Rock vs Mine Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11ZSZNA17rZpQ_px0nhksFl-8JfEGv4jx
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Data Collection and Data Processing

sonar_data = pd.read_csv('/content/sonar data.csv', header=None)

sonar_data.head()

sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts() # M- Mine, R- Rock

sonar_data.groupby(60).mean()

"""Seperating Data and Labels (Label here is the last column)"""

# axis=0 -> for row, axis=1 -> for column
X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

print(X)
print(Y)

"""Training and Testing data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

print(Y.shape, Y_train.shape, Y_test.shape)

print(X_train, Y_train)

"""Model Training - Logistic Regression (Generally this is the best model when it comes to binary categorical data problems)"""

model = LogisticRegression()

#Training the Logistic Regression model with the training data
model.fit(X_train, Y_train)

"""Model Evaluation - Calculating the accuracy"""

# Accuracy on training data

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data: ',training_data_accuracy)

# Accuracy on test data

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data: ',test_data_accuracy)

"""Making a predictive system

"""

input_data = (0.0526,0.0563,0.1219,0.1206,0.0246,0.1022,0.0539,0.0439,0.2291,0.1632,0.2544,0.2807,0.3011,0.3361,0.3024,0.2285,0.291,0.1316,0.1151,0.3404,0.5562,0.6379,0.6553,0.7384,0.6534,0.5423,0.6877,0.7325,0.7726,0.8229,0.8787,0.9108,0.6705,0.6092,0.7505,0.4775,0.1666,0.3749,0.3776,0.2106,0.5886,0.5628,0.2577,0.5245,0.6149,0.5123,0.3385,0.1499,0.0546,0.027,0.038,0.0339,0.0149,0.0335,0.0376,0.0174,0.0132,0.0103,0.0364,0.0208)

  #After getting the data, change it into numpy array for faster calculations

  input_data_as_numpy_array = np.asarray(input_data)

  #reshape the numpy array as we are predicting for one instance
  input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

  prediction = model.predict(input_data_reshaped)

  print(prediction)

  if (prediction[0] == 'R'):
    print('It is a Rock!')
  else:
    print('It is a Mine!!!')

