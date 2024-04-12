import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('traveldistance.csv')

df['Date'] = pd.to_datetime(df['Date'])

weekly = df.resample('W-Mon', on='Date').sum()

df_1 = weekly[weekly['Number of Trips 10-25'] > 10000000]

df_2 = weekly[weekly['Number of Trips 50-100'] > 10000000]

plt.figure(figsize=(12, 6))
plt.scatter(df_1.index, df_1['Number of Trips 10-25'], label='The dates that > 10000000 people conducted 10-25 Number of Trips', color='blue')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.title('Number of Trips 10-25')
plt.legend()
plt.grid(True)

plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(df_2.index, df_2['Number of Trips 50-100'], label='The dates that > 10000000 people conducted 50-100 Number of Trips', color='red')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.title('Number of Trips 50-100')
plt.legend()
plt.grid(True)

plt.show()
