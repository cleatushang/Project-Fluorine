# Project Fluorine

##
```
pip install sqlalchemy
```
pip install pandas
```
pip install yfinance
```

## Execute the Python
You can easily open the .py file by following code:
*change the path location of your own
```
exec(open("/Users/kylehang/Desktop/SP500.py").read())
```
### What this for?
After this, the SP500 list will gather from WIKIPEDIA lively
and also generate an local sql database file.

## How to view the database?
Use "DB Browser for SQLite" to view the database
or by SQL Query in python shell

### The SQL Query examples (python):
```
pd.read_sql('TSLA', USengine)
```

or check the date that close price larger then open price

```
pd.read_sql('SELECT * FROM TSLA WHERE Close > Open', USengine)
```

# Scheduling with Crontab
The idea basiclly is using Crontab(Mac/Linux), Task Scheduler(Windows) to run the python at scheduled time.
## Before the work
### Get Cron time format

```
https://crontab.guru/#0_5_*_*_*
```

### Get Python Path
Tell the Crontab where to how to open .py file
#### Run in terminal
```
where python
```
My example path like this:
```
/Users/kylehang/opt/anaconda3/envs/Stock/bin/python
```
## Start with Crontab
### Run in Terminal
```
env EDITOR=nano crontab -e
```
### Run in Nano
```
0 5 * * * cd Desktop && /Users/kylehang/opt/anaconda3/envs/Stock/bin/python SP500.py
```
Save and exit Nano, Then you may use 
```
crontab -l
```
To run the schedule
