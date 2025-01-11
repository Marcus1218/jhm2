import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Fetch stock data
ticker = input('Enter ticker symbol: ')
start_year = input ('Enter the start Year and month:(e.g 2020-01)')
end_year = input ('Enter the end Year and month:(e.g 2025-01)')
stock_data = yf.download(ticker, start=f'{start_year}-01', end=f'{end_year}-01')

# Prepare the data
stock_data = stock_data.dropna()
X = np.arange(len(stock_data)).reshape(-1, 1)
y = stock_data['Close'].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Linear regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Predict future prices with linear model
y_linear_pred = linear_model.predict(X_test)

# Polynomial regression model
poly_features = PolynomialFeatures(degree=4)
X_poly_train = poly_features.fit_transform(X_train)
X_poly_test = poly_features.transform(X_test)
poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)
y_poly_pred = poly_model.predict(X_poly_test)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data['Close'], label='Actual Prices')
plt.plot(stock_data.index[len(X_train):], y_linear_pred, label='Linear Predicted Prices', linestyle='--')
plt.plot(stock_data.index[len(X_train):], y_poly_pred, label='Polynomial Predicted Prices', linestyle='--')

# Overlay the regression line on the entire data
full_X = np.arange(len(stock_data)).reshape(-1, 1)
full_y_linear_pred = linear_model.predict(full_X)
full_X_poly = poly_features.transform(full_X)
full_y_poly_pred = poly_model.predict(full_X_poly)
plt.plot(stock_data.index, full_y_linear_pred, label='Linear Regression Line', color='red', linestyle='-.')
plt.plot(stock_data.index, full_y_poly_pred, label='Polynomial Regression Line', color='green', linestyle='-.')

plt.title(f'{ticker} Stock Prices Prediction')
plt.xlabel('Date')
plt.ylabel('Price USD')
plt.legend()
plt.show()


print("Stock Prediction Successful")