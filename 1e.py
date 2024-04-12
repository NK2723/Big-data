import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Tripfulldata.csv")


distance_columns = ["Trips <1 Mile", "Trips 1-25 Miles", "Trips 1-3 Miles", "Trips 10-25 Miles",
                    "Trips 100-250 Miles", "Trips 100+ Miles", "Trips 25-100 Miles", "Trips 25-50 Miles",
                    "Trips 250-500 Miles", "Trips 3-5 Miles", "Trips 5-10 Miles", "Trips 50-100 Miles",
                    "Trips 500+ Miles"]


total_participants = df[distance_columns].sum()


plt.figure(figsize=(10, 6))
total_participants.plot(kind='bar', color='green')
plt.title('Travellers by Distance-Trip')
plt.xlabel('Distance-Trip')
plt.ylabel('Total Travellers')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()