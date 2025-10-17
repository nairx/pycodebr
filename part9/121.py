import pandas as pd
score = [34,45,78]
series = pd.Series(score,index=["Sai","Suman","Gowtham"])
print(series)
print(series["Sai"])
print(series[0])