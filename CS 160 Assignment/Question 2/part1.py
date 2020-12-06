import pandas as pd 
data = pd.read_csv("04-26-2020.csv",index_col="Country/Region") 
data=data[['Confirmed', 'Deaths','Recovered','Active']]
print(data)
