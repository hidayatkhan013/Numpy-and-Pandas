import pandas as pd 
data = pd.read_csv("04-26-2020.csv") 
data=data[['Last_Update','Country/Region','Confirmed','Deaths','Recovered']]
print(data.head(10))