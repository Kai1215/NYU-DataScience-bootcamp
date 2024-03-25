import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = './Brooklyn_Bridge_Automated_Pedestrian_Counts_Demonstration_Project.csv'
data = pd.read_csv(file_path)
#print(df.head())

data['hour_beginning'] = pd.to_datetime(data['hour_beginning'])

# 1) Filter the data to include only weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
data['day_of_week'] = data['hour_beginning'].dt.day_name()
weekdays_data = data[data['day_of_week'].isin(weekdays)]

pedestrian_counts  = weekdays_data.groupby('day_of_week')['Pedestrians'].sum().reindex(weekdays)

plt.figure(figsize=(10, 5))
plt.plot(pedestrian_counts.index, pedestrian_counts.values, marker='o')
plt.title('Pedestrian Counts by Day of the Week (Weekdays Only)')
plt.xlabel('Day of the Week')
plt.ylabel('Total Pedestrian Counts')
plt.grid(True)
#plt.show()

# 2) Filter the data for the year 2019
import seaborn as sns

brooklyn_bridge_2019 = data[(data['location'] == 'Brooklyn Bridge') & (data['hour_beginning'].dt.year == 2019)]

weather_summary_encoded = pd.get_dummies(brooklyn_bridge_2019['weather_summary'])
encoded_data = pd.concat([weather_summary_encoded, brooklyn_bridge_2019['Pedestrians']], axis=1)

# Calculate correlation matrix
correlation_matrix = encoded_data.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Weather Summary and Pedestrian Counts')
#plt.show()

# 3) categorize time of day into morning, afternoon, evening, and night, and create a new column in the DataFrame to store these categories. 
def categorize_time_of_day(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 24:
        return 'Evening'
    else:
        return 'Night'

data['time_of_day'] = data['hour_beginning'].dt.hour.apply(categorize_time_of_day)

ped_counts_per_time_of_day = data.groupby('time_of_day')['Pedestrians'].sum()

print("Pedestrian Activity Patterns Throughout the Day:")
print(ped_counts_per_time_of_day)
