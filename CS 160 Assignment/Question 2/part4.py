import pandas as pd 
data = pd.read_csv("04-26-2020.csv") 
data=data[['Country/Region','Province_State','Recovered']]
is_rec =  data['Recovered']!=0
recoverd_data = data[is_rec]
print(recoverd_data)