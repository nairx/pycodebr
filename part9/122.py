import pandas as pd
score = {"Vinay":34,"Venkateshwara":45,"Lahari":78}
# series = pd.Series(score)
series = pd.Series(score,index=["Vinay","Lahari"])
print(series)