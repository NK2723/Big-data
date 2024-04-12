import pandas as pd

# Load the first CSV file
df = pd.read_csv('traveldistance.csv')

# Count the unique values for the "Week" column
unique_week = df['Week'].nunique()

# Calculate the average population staying at home per week
pop_home = df.groupby(by='Week')['Population Staying at Home'].mean()

# Print the unique week count for the first dataset
print("Week Count:", unique_week)

# Print the average population staying at home per week for the first dataset
print("Average Population Staying at Home per Week:")
print(pop_home)

# Load the second CSV file
df1 = pd.read_csv('Tripfulldata.csv')

# Compute the number of unique values for the "Week" column in the second dataset
unique_week_count_2 = df1['Week of Date'].nunique()

# Group and compute the mean of 'Trips 1-25 Miles' column per week for the second dataset
mean_trips = df1.groupby(by='Week of Date')['Trips 1-25 Miles'].mean()

# Print the computed results for the second dataset
print("Week Count:", unique_week_count_2)
print("Mean Trips 1-25 Miles per Week:", mean_trips)


import matplotlib.pyplot as plt

df = pd.read_csv('traveldistance.csv')
plt.figure(figsize=(10, 6))
plt.hist(df['Week'], bins=20, color='red', alpha=0.7)
plt.xlabel('Week')
plt.ylabel('Frequency')
plt.title('People Staying at Home per Week')
plt.grid(True)
plt.show()

df = pd.read_csv('Tripfulldata.csv')
trip_distances = [
    'Trips 1-25 Miles', 'Trips 1-3 Miles', 'Trips 10-25 Miles',
    'Trips 100-250 Miles', 'Trips 100+ Miles', 'Trips 25-100 Miles',
    'Trips 25-50 Miles', 'Trips 250-500 Miles', 'Trips 3-5 Miles',
    'Trips 5-10 Miles', 'Trips 50-100 Miles', 'Trips 500+ Miles'
]

plt.figure(figsize=(12, 8))
for distance in trip_distances:
    plt.scatter(df[distance], df['Population Staying at Home'], label=distance)
plt.xlabel('Travel Distances')
plt.ylabel('People Staying at Home')
plt.title('Comparison between People Staying at Home and Travel Distances')
plt.legend()
plt.grid(True)
plt.show()
