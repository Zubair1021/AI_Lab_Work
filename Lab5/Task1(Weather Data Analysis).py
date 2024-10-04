import pandas as pd

import numpy as np

import random as rand

import matplotlib.pyplot as plt


temp=[]
hum=[]
Wind_speed=[]
weather=[]
day=[]
condition=["Sunny","Rainy","Cloudy","Clear","ThunderStrom"]
Total_Days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]



for i in range(1,366):
    temp.append(rand.randint(10,40))
    hum.append(rand.randint(30, 90))
    Wind_speed.append(rand.randint(0, 20))
    weather.append(condition[rand.randint(0, 4)])
    day.append(Total_Days[rand.randint(0, 6)])
    
    
    
data = {
"Tempurature": temp,
"Humidity":hum,
"Wind Speed":Wind_speed,
"Weather":weather,
"Day":day
        
}    


#print(pd.DataFrame(data,index=np.arange(1,366)))


#Mean/Median/Standard Deviaton

data_frame = pd.DataFrame(data,index=np.arange(1,366))


print(data_frame)


temp_array = np.array(data_frame ['Tempurature'])

mean = np.mean(temp_array)

print("Mean of the Tempurature is :\n",mean)


median= np.median(temp_array)

print("Median of the Tempurature is :\n",median)


STD = np.std(temp_array)

print("Standard Deviation of the Tempurature is :\n",STD)


#Hot days Count


sunny_hot_days = data_frame[(data_frame["Tempurature"] > 30) & (data_frame["Weather"] == "Sunny")]

hot_days_Total = len(sunny_hot_days)

print("Total Hot days: ",hot_days_Total)



#Group the data set 

avg_humidity_per_weather = data_frame.groupby("Weather")["Humidity"].mean()

print(avg_humidity_per_weather)


#Temperature Variation Graph

plt.title('Temperature Variation Over the Year')
plt.plot(temp_array)
plt.xlabel('Days')
plt.ylabel('Tempurature')
plt.show()


# Number of Days for Each Weather Day

weather_counts = data_frame["Weather"].value_counts()


plt.bar(weather_counts.index, weather_counts.values, color=['yellow', 'blue', 'gray', 'cyan', 'purple'])
plt.title('Number of Days for Each Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Days')
plt.show()





