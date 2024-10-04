import numpy as np
import pandas as pd
import random as rand
import matplotlib.pyplot as plt



company_names=['comp1','comp2','comp3','comp4','comp5']

Date=[]
Open_price=[]
Close_price=[]
volume_Traded=[]
company=[]


for i in range(1,1001):
    Open_price.append(rand.randint(50, 500))
    Close_price.append(rand.randint(50, 500))
    volume_Traded.append(rand.randint(100, 1000000))
    company.append(company_names[rand.randint(0, 4)])
    
    d = np.datetime64("2021-10-02")
    d += np.random.randint(0, 730)
    Date.append(d)
    
    
    
    
    
data={
"Company":company,
"Volume Traded":volume_Traded,
"Open Price":Open_price,
"Close Price":Close_price,
"Date":Date      
}

Data_frame= pd.DataFrame(data,index=np.arange(1,1001))
print(Data_frame)


close_price_array = np.array(Data_frame["Close Price"])
price_diff = np.diff(close_price_array)
previous_price = close_price_array[:-1]
daily_pct_change = (price_diff / previous_price) * 100
print(daily_pct_change)


group_data = Data_frame.groupby("Company").sum(True)["Volume Traded"]
print(group_data)


plt.title('Close Price over time for a particular company')
plt.plot(close_price_array)
plt.xlabel('Days')
plt.ylabel('Tempurature')
plt.show()



