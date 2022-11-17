import numpy as np
import pandas as pd

df = pd.read_csv("Data1/kospi_data.csv", index_col = 0, header = 0)
print(df)
print(df.shape)

df = df.sort_values(['Date'], ascending = True)

df = df.values

np.save('Data1/kospi_data.npy', arr = df)