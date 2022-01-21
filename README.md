# Project Fluorine

## Execute the Python
You can easily open the .py file by following code:
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
