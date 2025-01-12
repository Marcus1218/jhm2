import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from datetime import datetime, timedelta

# Fetch stock data
ticker = input('Enter ticker symbol: ')
start_year = input('Enter the start Year and month:(e.g 2020-01)')
end_year = input('Enter the end Year and month:(e.g 2025-01)')
if start_year == '':
    start_year = '2020-01'
if end_year == '':
    end_year = datetime.now().strftime('%Y-%m')
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

# Polynomial regression model (degree 2)
poly_features_2 = PolynomialFeatures(degree=2)
X_poly_train_2 = poly_features_2.fit_transform(X_train)
X_poly_test_2 = poly_features_2.transform(X_test)
poly_model_2 = LinearRegression()
poly_model_2.fit(X_poly_train_2, y_train)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data['Close'], label='Actual Prices (Full)')

# Overlay the regression line on the entire data
full_X = np.arange(len(stock_data)).reshape(-1, 1)
full_y_linear_pred = linear_model.predict(full_X)
full_X_poly_2 = poly_features_2.transform(full_X)
full_y_poly_pred_2 = poly_model_2.predict(full_X_poly_2)
plt.plot(stock_data.index, full_y_linear_pred, label='Linear Regression Trend', color='red', linestyle='-.')
plt.plot(stock_data.index, full_y_poly_pred_2, label='Polynomial Regression Trend (Degree 2)', color='blue', linestyle='-.')

# Plot selected actual prices
plt.plot(stock_data.index[:len(X_train)], stock_data['Close'][:len(X_train)], label='Actual Prices (Selected)', color='green')

# Predict future prices (2 years)
future_dates = [stock_data.index[-1] + timedelta(days=i) for i in range(1, 731)]
future_X = np.arange(len(stock_data) + 730).reshape(-1, 1)
future_y_linear_pred = linear_model.predict(future_X[-730:])
future_X_poly_2 = poly_features_2.transform(future_X[-730:])
future_y_poly_pred_2 = poly_model_2.predict(future_X_poly_2)
plt.plot(future_dates, future_y_linear_pred, label='Linear Regression (Prediction)', color='red', linestyle='--')
plt.plot(future_dates, future_y_poly_pred_2, label='Polynomial Regression (Prediction)', color='blue', linestyle='--')

plt.title(f'{ticker} Stock Prices Prediction')
plt.xlabel('Date')
plt.ylabel('Price USD')
plt.legend()
plt.show()

print("Stock Prediction Successful")