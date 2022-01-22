# # Author: Kyle_Hang
# For Personal Use ONLY!

# In[6] import required

import sqlalchemy
import pandas as pd
import yfinance as yf
import pymysql

# In[12] Define wiki's address

wiki = 'https://en.wikipedia.org/wiki/'

# In[16] Pulling S&P 500 companies list

tickersUS = pd.read_html(wiki+'List_of_S%26P_500_companies')[0].Symbol.to_list()

# In[20]: looping download stock price from Yahoo Finance

def getdata(tickers):
    data = []
    for ticker in tickers:
        data.append(yf.download(ticker).reset_index())
    return data

# In[28]: Define 'US'

US = getdata(tickersUS)

# The above is done for downloading all stock data.

print('Successfully Downloaded',len(US),'Stocks')

engine = sqlalchemy.create_engine('mysql+pymysql://root:1234@34.92.106.78/Stocks')

def TOSQL(frames,symbols, engine):
    for frame,symbol in zip(frames,symbols):
        frame.to_sql(symbol, engine, index=False, if_exists='append')
    print('Successfully imported data')

# In[53]: Transfer Datas into SQL database

TOSQL(US, tickersUS, engine)
