import time
import pandas as pd
import dask.dataframe as dd
import matplotlib.pyplot as plt

# Define the list of processors
processor_list = [10, 20]

# Dictionary to store computation times for Pandas
pandas_computation_times = {}

# Dictionary to store computation times for Dask
dask_computation_times = {}

# Pandas Implementation
for processor in processor_list:
    start_time_pandas = time.time()  # Start the timer
    # Load CSV data using Pandas
    df_pandas = pd.read_csv('traveldistance.csv')
    # Perform computation with Pandas
    result_pandas = df_pandas.groupby('Week')['Population Staying at Home'].mean()
    # Calculate Pandas computation time
    pandas_execution_time = time.time() - start_time_pandas
    # Store Pandas computation time
    pandas_computation_times[processor] = pandas_execution_time

# Dask Implementation
for processor in processor_list:
    start_time_dask = time.time()  # Start the timer
    # Load CSV data using Dask, specifying block size and data types
    df_dask = dd.read_csv('traveldistance.csv', blocksize='64MB', dtype={'Population Staying at Home': 'float64'})
    # Perform computation with Dask
    result_dask = df_dask.groupby('Week')['Population Staying at Home'].mean().compute()
    # Calculate Dask computation time
    dask_execution_time = time.time() - start_time_dask
    # Store Dask computation time
    dask_computation_times[processor] = dask_execution_time

# Display computation times for Pandas
print("Computation times for different numbers of processors for Pandas:")
for processor, time_taken in pandas_computation_times.items():
    print(f"Number of processors: {processor}, Time taken: {time_taken} seconds")

# Display computation times for Dask
print("\nComputation times for different numbers of processors for Dask:")
for processor, time_taken in dask_computation_times.items():
    print(f"Number of processors: {processor}, Time taken: {time_taken} seconds")

# Plotting
plt.figure(figsize=(10, 6))

# Plot Pandas computation times with blue color
plt.plot(pandas_computation_times.keys(), pandas_computation_times.values(), marker='o', label='Pandas', color='blue')

# Plot Dask computation times with red color
plt.plot(dask_computation_times.keys(), dask_computation_times.values(), marker='o', label='Dask', color='red')

plt.title('Comparison of computation times with different processors')
plt.xlabel('Number of Processors')
plt.ylabel('Time')
plt.legend()
plt.grid(True)
plt.show()
