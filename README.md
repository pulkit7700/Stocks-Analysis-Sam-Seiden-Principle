# Stock Exchange Dashboard

This Python code provides a Stock Exchange Dashboard using Streamlit. It allows users to visualize stock data, analyze price movements, explore fundamental data, and read news related to a particular stock.

## Prerequisites
Before running the code, make sure you have the following libraries installed:

- Streamlit
- Pandas
- NumPy
- Matplotlib
- Module (custom module containing `demand_and_supply_principle` function)
- yfinance
- Plotly Express
- datetime
- stocknews

You can install these libraries using pip:
```
pip install streamlit pandas numpy matplotlib yfinance plotly datetime stocknews
```

**Note**: The code uses the Vantage API (Free), which allows only 5 calls per minute and 500 calls per day.

## Usage
To run the code, execute the Python script in your preferred Python environment. Make sure you have an active internet connection.

Upon running the code, a Streamlit app will be launched, presenting a user interface with several options and visualizations.

### Stock Selection
- Enter the stock name in the text input field provided in the sidebar.
- Select the start and end dates for the stock data using the date input fields in the sidebar.

### Pricing Data
- Displays price movements of the selected stock.
- The price data is visualized using a line chart.
- It also shows the annual return, standard deviation, and risk-adjusted return.

### Fundamental Data
- Displays fundamental data of the selected stock, including balance sheet, income statement, and cash flow statement.
- The data is fetched using the `yfinance` library.

### News
- Displays the latest news related to the selected stock.
- The news is obtained using the `stocknews` library.

### Price Recommendor
- Allows users to input the price and volume of the stock.
- The algorithm uses these values to predict the recommended price to invest.
- Clicking the "Predict Amount" button triggers the prediction.

**Note**: The algorithm automatically takes the latest price and volume values from the data and fits them to the prediction model.

## Visualization Compatibility
If you are unable to see the charts, please try a different browser, as visualization is not supported on all browsers.

Please note that this code is provided as an example and may require modifications or improvements to suit your specific use case.
