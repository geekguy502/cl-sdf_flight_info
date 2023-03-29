#include the necessary libs
import pandas as pd
import matplotlib 
from matplotlib import pyplot as plt

arrivals = pd.read_csv('./combined_data/arrivals.csv', usecols=['airline', 'arr_year', 'total_arrivals'])
departures = pd.read_csv('./combined_data/departures.csv', usecols=['airline', 'dep_year', 'total_departures'])

#View some of the arrival data to verify it has loaded properly.
print(arrivals.head(10))
print(arrivals.info())
print(arrivals.shape)

#plot the arrival data
arrivals['arr_year'] = arrivals['arr_year'].astype(int)
arrivals.groupby(['arr_year', 'airline']).sum()['total_arrivals'].unstack().plot(kind='line', ylabel='# of flights')
plt.xticks(arrivals['arr_year'].unique())
plt.xlabel('Year')
plt.title('Total SDF arrivals by Year')
plt.show()

#View some of the departure data to verify it has loaded properly.
print(departures.head(10))
print(departures.info())
print(departures.shape)

#plot the departure data
departures['dep_year'] = departures['dep_year'].astype(int)
departures.groupby(['dep_year', 'airline']).sum()['total_departures'].unstack().plot(kind='line', ylabel='Total flights')
plt.xticks(departures['dep_year'].unique())
plt.xlabel('Year')
plt.title('Total SDF Departures by Year')
plt.show()