import pandas as pd
df = pd.read_csv(".\part9\mydata.csv")
# print(df)
# print(df["Vinay"])
pd.options.display.max_rows=1
pd.options.display.max_columns=1
print(df)
# print(pd.options.display.max_rows)