import pandas as pd 
data = pd.read_csv("04-26-2020.csv") 
data=data[['Country/Region','Province_State','Recovered']]
is_not_rec =  data['Recovered']==0
not_recoverd_data = data[is_not_rec]
print(not_recoverd_data)