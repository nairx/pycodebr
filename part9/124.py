import pandas as pd
score = {"Vinay":[34,45],"Venkateshwara":[45,30],"Lahari":[78,90]}
df = pd.DataFrame(score,index=["Python","Java"])
# print(df)
# df.to_csv(".\part9\mydata.csv",index=False)
print(df.loc["Python"])
# print(df["Vinay"])
