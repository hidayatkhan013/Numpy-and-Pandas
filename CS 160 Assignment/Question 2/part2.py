import pandas as pd 
data = pd.read_csv("04-26-2020.csv") 
data=data[['Country/Region','Province_State','Confirmed', 'Deaths','Recovered','Active']]
is_Us =  data['Country/Region']=='US'
Us_data = data[is_Us]
print(Us_data)
