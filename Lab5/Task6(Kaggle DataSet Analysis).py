import pandas as pd
import matplotlib.pyplot as plt


Data_frame = pd.read_csv('Summer-Olympic-medals-1976-to-2008.csv', encoding='ISO-8859-1')
print(Data_frame)


#------Filteration Operations


#Find Gold Data
gold_data = Data_frame[Data_frame['Medal']=='Gold']
print("The Gold medalist Data: \n",gold_data)

#Find Data of USA Country 

pak_data = Data_frame[Data_frame['Country_Code']=='PAK']
print("The Pakistan data : \n",pak_data)


#Filter USA data in year 2008

filter_usa_data = Data_frame[(Data_frame['Country_Code']=='USA') & (Data_frame['Year']==2008)]
print("The USA data in 2008 year: \n",filter_usa_data)


#Filter a specific sport 

filter_sport = Data_frame[Data_frame['Sport']=='Hockey']
print("The Hockey data is: \n",filter_sport)


#------GroupBy Operations

# Group by 'Country' and 'Year' to get medal counts
medals_by_country_year = Data_frame.groupby(['Country', 'Year']).size().reset_index(name='Medal Count')
print(medals_by_country_year)

#Pakitan Gold medal Counts
medals_pak_count = pak_data.groupby(['Country','Year']).size().reset_index(name="Medal Count")
print(medals_pak_count)


#------Graph Operations


# Line chart: Medals won by USA over the years
usa_medals_by_year = Data_frame[Data_frame['Country_Code'] == 'USA'].groupby('Year').size()
usa_medals_by_year.plot(kind='line', marker='o',color='red')
plt.title('Medals won by USA over the years')
plt.ylabel('Number of Medals')
plt.show()

# Bar chart: Top 5 countries by total medals
top_countries = Data_frame['Country'].value_counts().head(5)
top_countries.plot(kind='bar', color='Green')
plt.title('Top 5 Countries by Total Medals')
plt.ylabel('Number of Medals')
plt.show()


# Histogram: Distribution of medals by year
plt.hist(Data_frame['Year'], bins=30, color='orange')
plt.title('Distribution of Medals by Year')
plt.xlabel('Year')
plt.ylabel('Number of Medals')
plt.show()


