import pandas as pd
df = pd.read_csv('.\part9\mydata.csv')
# print(df)
# print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df)