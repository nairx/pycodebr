import pandas as pd
df = pd.read_csv(".\part9\mydata.csv")
print(df)
df["doj"]=pd.to_datetime(df['doj'])
print(df)