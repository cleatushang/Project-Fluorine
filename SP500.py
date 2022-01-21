# # Author: Kyle_Hang
# For Personal Use ONLY!

# In[6] import required

import sqlalchemy
import pandas as pd
import yfinance as yf

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

# In[36]: The following will create an SQL database

def createengine(name):
    engine = sqlalchemy.create_engine('sqlite:///'+name)
    return engine

# In[42]: Define USengine

USengine = createengine('USA')

# In[46]: Store dataframe into SQL and create tables by Symbols name

def TOSQL(frames,symbols, engine):
    for frame,symbol in zip(frames,symbols):
        frame.to_sql(symbol, engine, index=False)
    print('Successfully imported data')

# In[53]: Transfer Datas into SQL database

TOSQL(US, tickersUS, USengine)
