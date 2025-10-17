import pandas as pd
df = pd.read_csv('.\part9\mydata.csv')
# df.loc[1,'age']=26 #correct age from 167 to 26
for r in df.index:
    if df.loc[r,'Vinay']>40:
        # df.loc[r,'Vinay']=0
        df.drop(r, inplace = True) #remove row
print(df.to_string())
