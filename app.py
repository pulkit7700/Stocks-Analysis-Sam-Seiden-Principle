import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Module import demand_and_supply_principle
import yfinance as yf
import plotly.express as px
import datetime as dt 




st.title("Stock Exchange Dashboard") 
st.info("The Only Issues is the Vantage API (Free) allows only 5 call per minute and 500 calls per Day.")

# Elements for the App
tick = st.sidebar.text_input("Enter Stock Name", value='AAPL')
start_date = st.sidebar.date_input('Start Date', value=dt.date(2010, 5, 1))
end_date = st.sidebar.date_input('End Date', value=dt.datetime.today())

# Data Stores

data = yf.download(tick, start=start_date, end=end_date)
fig = px.line(data, x=data.index, y=data["Adj Close"], title=tick)
st.plotly_chart(fig)
st.info("If you are unable to see the Charts please try a different Browser as Visualization is not supported on  yout browser")
pricing_data, fundamental_data, news = st.tabs(["Pricing Data", "Fundamental Data", "News"])

# Tabs

with pricing_data:
    st.header('Price Movements')
    data2 = data
    data2["% Change"] = data['Adj Close'] / data['Adj Close'].shift(1)
    data2.dropna(inplace=True)
    st.write(data2)
    st.write("Annual Return is {}".format(data2["% Change"].mean()*252*100), "%")
    st.write("Standard deviation is {}".format(np.std(data2["% Change"])*np.sqrt(252)*100), "%")
    st.write("Risk Adj. Return is {}".format((data2["% Change"].mean()*252*100) /(np.std(data2["% Change"])*np.sqrt(252)*100)))
    
# from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:

    # Trying with yfinance
    stock = yf.Ticker(tick)
    st.subheader('Balance Sheet')
    balance_sheet = stock.balance_sheet.T
    st.write(balance_sheet)
    st.subheader('Income Statement')
    Income_Statement = stock.income_stmt.T
    st.write(Income_Statement)
    st.subheader('Cash Flow Statement')
    Cash_flow = stock.cashflow.T
    st.write(Cash_flow)

from stocknews import StockNews
with news:
    st.header(f'News of the {tick}')
    sn = StockNews(tick, save_news=False)
    df_news = sn.read_rss()
    for i in range(10):
        st.subheader('New {} -  {}'.format(i + 1, df_news['title'][i]))
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.success(f'Title Sentiment {title_sentiment}')
        news_sentiment = df_news['sentiment_summary'][i]
        st.success(f'News Sentiment {news_sentiment}')
    st.write('News')

# number selector for Price and Volume

st.title('Price Recomendor')

# Display Checks for the Apps
Price_value = (data2.iloc[-1]["Close"])
Volume_Value = (data2.iloc[-1]["Volume"])

st.info('Note : The Algorithm automatically takes the values from the data an put on the Price abd Volume values and fits its to the prediction model')

Price = st.number_input('Enter Price of the Stock', value=Price_value)
Volume = st.number_input('Enter Volume of the Stock', value=Volume_Value)
def prediction():
    predicted_price = demand_and_supply_principle(Price, Volume)
    st.success("The Predicted Price that you should invest is {}".format(predicted_price))
    return predicted_price

if st.button('Predict Amount', on_click=prediction):
    st.snow()
    prediction()
