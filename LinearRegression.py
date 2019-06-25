import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv('C:/Python_devenv/Data/HousePricesKaggle/housing-prices-dataset/train.csv')
df_test = pd.read_csv('C:/Python_devenv/Data/HousePricesKaggle/housing-prices-dataset/test.csv')
#print(df.head())

# Print column names
#for col in df.columns:
#	print(col)

X_train = df_train[['GrLivArea']] # GarageArea, PoolArea
Y_train = df_train['SalePrice']

X_test = df_test[['GrLivArea']]

# Print scatter plot of the features/inputs/predictors
#plt.scatter(X['GrLivArea'], X['GarageArea'])
#plt.show()

# Fit a linear regression model using ordinary least squares
model = LinearRegression().fit(X_train, Y_train)
y_pred = model.predict(X_test)

plt.scatter(X_train, Y_train)
plt.plot(X_test, y_pred, color='red')
plt.show()
