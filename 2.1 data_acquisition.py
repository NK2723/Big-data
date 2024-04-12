import pandas as pd

df = pd.read_csv("Tripfulldata.csv")
print(df.head())

import dask.dataframe as dd

ddf = dd.read_csv("Tripfulldata.csv")
print(ddf.head())