import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV file into a DataFrame
df = pd.read_csv(r'E:\bike sharing\2018Combined.csv')

# Convert 'Start Time' column to datetime format
df['Start Time'] = pd.to_datetime(df['Start Time'])

# Additional Visualizations

# 1. Hourly Usage Patterns
plt.figure(figsize=(10, 6))
df['Hour'] = df['Start Time'].dt.hour
sns.countplot(data=df, x='Hour', palette='muted')
plt.title('Hourly Usage Patterns')
plt.xlabel('Hour of the Day')
plt.ylabel('Count')
plt.show()

# 2. Weekday vs. Weekend Usage
plt.figure(figsize=(8, 6))
df['Day of Week'] = df['Start Time'].dt.dayofweek
df['Weekend'] = df['Day of Week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
sns.countplot(data=df, x='Weekend', palette='pastel')
plt.title('Weekday vs. Weekend Usage')
plt.xlabel('')
plt.ylabel('Count')
plt.show()

# 3. Trip Duration by User Type
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='User Type', y='Trip  Duration in Minutes', palette='Set2')
plt.title('Trip Duration by User Type')
plt.xlabel('User Type')
plt.ylabel('Trip Duration (minutes)')
plt.show()

# 4. Station Analysis (Top Start Stations)
plt.figure(figsize=(12, 8))
top_start_stations = df['Start Station'].value_counts().head(10)
sns.barplot(x=top_start_stations.values, y=top_start_stations.index, palette='rocket')
plt.title('Top 10 Start Stations')
plt.xlabel('Number of Rides')
plt.ylabel('Station')
plt.show()
