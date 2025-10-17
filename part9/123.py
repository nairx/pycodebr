import pandas as pd
score = {"Vinay":[34,45],"Venkateshwara":[45,30],"Lahari":[78,90]}
df = pd.DataFrame(score,index=["Python","Java"])
# print(df)
print(df["Vinay"])
