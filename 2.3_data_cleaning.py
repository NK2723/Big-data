import pandas as pd
import dask.dataframe as dd

traveldistance = pd.read_csv("traveldistance.csv")
columns_traveldistance = ["Level", "Date", "State FIPS", "State Postal Code", "County FIPS", "County Name",
                              "Population Staying at Home", "Population Not Staying at Home", "Number of Trips",
                              "Number of Trips <1", "Number of Trips 1-3", "Number of Trips 3-5",
                              "Number of Trips 5-10", "Number of Trips 10-25", "Number of Trips 25-50",
                              "Number of Trips 50-100", "Number of Trips 100-250", "Number of Trips 250-500",
                              "Number of Trips >=500", "Row ID", "Week", "Month"]

Tripfulldata = pd.read_csv("traveldistance.csv")
columns_Tripfulldata = ["Month of Date", "Week of Date", "Year of Date", "Level", "Date", "Week Ending Date",
                              "Trips <1 Mile", "People Not Staying at Home", "Population Staying at Home",
                              "Trips", "Trips 1-25 Miles", "Trips 1-3 Miles", "Trips 10-25 Miles",
                              "Trips 100-250 Miles", "Trips 100+ Miles", "Trips 25-100 Miles", "Trips 25-50 Miles",
                              "Trips 250-500 Miles", "Trips 3-5 Miles", "Trips 5-10 Miles", "Trips 50-100 Miles",
                              "Trips 500+ Miles"]

missing_values_traveldistance = traveldistance.isnull().sum()
missing_values_Tripfulldata = Tripfulldata.isnull().sum()

duplicate_rows_traveldistance = traveldistance.duplicated().sum()
duplicate_rows_Tripfulldata = Tripfulldata.duplicated().sum()

dtype_traveldistance = {'County Name': 'object', 'Number of Trips': 'float64', 'Number of Trips 1-3': 'float64',
                            'Number of Trips 10-25': 'float64', 'Number of Trips 100-250': 'float64',
                            'Number of Trips 25-50': 'float64', 'Number of Trips 250-500': 'float64',
                            'Number of Trips 3-5': 'float64', 'Number of Trips 5-10': 'float64',
                            'Number of Trips 50-100': 'float64', 'Number of Trips <1': 'float64',
                            'Number of Trips >=500': 'float64', 'Population Not Staying at Home': 'float64',
                            'Population Staying at Home': 'float64', 'State Postal Code': 'object'}

traveldistance_dask = dd.read_csv("traveldistance.csv", dtype=dtype_traveldistance)
Tripfulldata_dask = dd.read_csv("Tripfulldata.csv")

missing_values_traveldistance_dask = traveldistance_dask.isna().sum().compute()
missing_values_Tripfulldata_dask = Tripfulldata_dask.isna().sum().compute()

traveldistance_dask_unique = traveldistance_dask.drop_duplicates()
duplicate_rows_traveldistance_dask = traveldistance_dask.shape[0].compute() - traveldistance_dask_unique.shape[0].compute()

Tripfulldatadask_unique = Tripfulldata_dask.drop_duplicates()
duplicate_rows_Tripfulldata_dask = Tripfulldata_dask.shape[0].compute() - Tripfulldatadask_unique.shape[0].compute()

print("Missing values in traveldistance.csv (Pandas):")
print(missing_values_traveldistance)
print("\nMissing values in Tripfulldata.csv (Pandas):")
print(missing_values_Tripfulldata)
print("\nNumber of duplicate rows in traveldistance.csv (Pandas):", duplicate_rows_traveldistance)
print("Number of duplicate rows in Tripfulldata.csv (Pandas):", duplicate_rows_Tripfulldata)
print("\nMissing values in traveldistance (Dask):")
print(missing_values_traveldistance_dask)
print("\nMissing values in Tripfulldata.csv (Dask):")
print(missing_values_Tripfulldata_dask)
print("\nNumber of duplicate rows in traveldistance.csv (Dask):", duplicate_rows_traveldistance_dask)
print("Number of duplicate rows in Tripfulldata.csv (Dask):", duplicate_rows_Tripfulldata_dask)