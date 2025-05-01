import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from darts import TimeSeries
from darts.models import TransformerModel
from datetime import datetime, timedelta
import torch
import time
import sys

# Start measuring time
start_time = time.time()

# Fetch stock data
ticker = input('Enter ticker symbol: ')
if ticker == '0':
    print("Ticker symbol cannot be 0. Exiting the program.")
    sys.exit(1)

start_year = '2020'
end_year = '2025'

try:
    stock_data = yf.download(ticker, start=f'{start_year}-01-01', end=f'{end_year}-01-01')
    if stock_data.empty:
        print("No data fetched. Exiting the program.")
        sys.exit(1)
    print("Stock data fetched")
except Exception as e:
    raise RuntimeError("Make sure you connect to the network") from e

# Prepare the data
stock_data = stock_data[['Close']].dropna()
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(stock_data).astype(np.float32)  # Convert to float32
print("Data scaled")

# Create a TimeSeries object
series = TimeSeries.from_dataframe(pd.DataFrame(scaled_data, columns=['Close']), time_col=None, value_cols=['Close'])
print("TimeSeries object created")

# Split the data into training and testing sets
train_size = int(len(series) * 0.8)
train_series = series[:train_size]
print("Data split into training and testing sets")

# Determine the device
if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"
print(f"Using device: {device}")

# Build the Transformer model
model = TransformerModel(
    input_chunk_length=60,
    output_chunk_length=1,
    n_epochs=30,  # Train the model 30 times
    model_name="transformer",
    nr_epochs_val_period=1,
    d_model=64,
    nhead=4,
    num_encoder_layers=2,
    num_decoder_layers=2,
    dim_feedforward=128,
    dropout=0.1,
    activation="relu",
    random_state=42,
    pl_trainer_kwargs={"accelerator": device}  # Ensure the model uses the appropriate device
)
print("Transformer model built")

# Train the model
model.fit(train_series)
print("Model trained")

# Number of days to predict (3 years)
n_days = 2 * 365

# Make predictions for the next 3 years
future_predict = model.predict(n=n_days, series=train_series)
print(f"Future predictions made for {n_days} days")

# Transform back to original form
future_predict = scaler.inverse_transform(future_predict.values())
print("Future predictions transformed back to original scale")
print("Future predictions:", future_predict)

# Linear regression
X = np.arange(len(stock_data)).reshape(-1, 1)
y = scaler.inverse_transform(scaled_data)
linear_model = LinearRegression()
linear_model.fit(X, y)
linear_predict = linear_model.predict(np.arange(len(stock_data) + n_days).reshape(-1, 1))
print("Linear regression predictions:", linear_predict)

# Polynomial regression (degree 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(np.arange(len(stock_data)).reshape(-1, 1))
poly_model = LinearRegression()
poly_model.fit(X_poly, y)
poly_predict = poly_model.predict(poly.fit_transform(np.arange(len(stock_data) + n_days).reshape(-1, 1)))
print("Polynomial regression predictions (degree 2):", poly_predict)

# Use the average of linear and polynomial regression predictions for future prices
future_predict = (linear_predict[len(stock_data):] + poly_predict[len(stock_data):]) / 2

# Plot the results
plt.figure(figsize=(12, 6))
actual_dates = stock_data.index
future_dates = pd.date_range(start=actual_dates[-1] + timedelta(days=1), periods=n_days, freq='D')

# Debug prints
print("Actual dates:", actual_dates)
print("Future dates:", future_dates)

# Highlight the previous year's stock prices
previous_year_start = max(actual_dates[0], actual_dates[-1] - timedelta(days=365))
previous_year_data = stock_data[previous_year_start:]

# Combine actual and future data for continuous line
combined_dates = actual_dates.union(future_dates)
combined_prices = np.concatenate((scaler.inverse_transform(scaled_data).flatten(), future_predict.flatten()))

plt.plot(actual_dates, stock_data['Close'], label='Actual Prices', linestyle='-', color='green')
plt.plot(previous_year_data.index, previous_year_data['Close'], label='Previous Year Prices', linestyle='-', color='black')
plt.plot(future_dates, future_predict, label='Future Prices', linestyle=':', color='green')
plt.plot(combined_dates, linear_predict.flatten(), label='Linear Regression Prices', linestyle='-.', color='red')
plt.plot(combined_dates, poly_predict.flatten(), label='Polynomial Regression Prices (Degree 2)', linestyle='--', color='blue')
plt.xlim([datetime.strptime(start_year, '%Y'), future_dates[-1]])
plt.title(f'Stock Prices Prediction ({ticker.upper()})')
plt.xlabel('Date')
plt.ylabel('Price USD')
plt.legend()
plt.show()


# End measuring time and print runtime
end_time = time.time()
print("------------------------------------------------")
print(f"Total runtime: {end_time - start_time} seconds")
print("Stock Prediction Successful")
print("------------------------------------------------")