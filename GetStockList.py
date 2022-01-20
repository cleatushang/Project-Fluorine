#!/usr/bin/env python
# coding: utf-8
# # Welcome to Jupyter!

# In[5]:

import sqlalchemy
import pandas as pd
import yfinance as yf
import csv

# In[8]:
# **enter the stock csv file location**
with open("/Users/kylehang/Desktop/tickersUS.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    tickersUS = list(reader)

# In[10]:


def getdata(tickers):
    data = []
    for ticker in tickers:
        data.append(yf.download(ticker).reset_index())
    return data


# In[11]:


US = getdata(tickersUS)

