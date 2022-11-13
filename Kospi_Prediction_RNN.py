import numpy as np
import pandas as pd

df1 = pd.read_csv("Data2/000020.csv", index_col = 0, header = 0)
#print(df1)
#print(df1.shape)

df2 = pd.read_csv("Data2/000030.csv", index_col = 0, header = 0)
#print(df2)
#print(df2.shape)

for i in range(len(df1.index)):
    df1.iloc[i, 4] = int(df1.iloc[i, 4].replace(',', ''))
    
for i in range(len(df2.index)):
    for j in range(len(df.iloc[i])):
        df2.iloc[i, j] = int(df2.iloc[i, j].replace(',', ''))
        
df1 = df1.sort_values(['일자'], ascending = True)
df2 = df2.sort_values(['일자'], ascending = True)

print(df1)
print(df2)