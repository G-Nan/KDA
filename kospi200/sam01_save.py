# 챕터 11, 삼성전자 주가 예측입니다.

import numpy as np
import pandas as pd

df1 = pd.read_csv("data\kospi200.csv", index_col=0, 
                  header=0, encoding='cp949', sep=',')
# 경로에 주의해 주세요. 경로에서 꼭 틀립니다.                     
print(df1)
print(df1.shape)

df2 = pd.read_csv("data\samsung.csv", index_col=0, 
                  header=0, encoding='cp949', sep=',')   
print(df2)
print(df2.shape)

# kospi200의 거래량
for i in range(len(df1.index)):     # 거래량 str -> int 변경
        df1.iloc[i,4] = int(df1.iloc[i,4].replace(',', ''))  
# 삼성전자의 모든 데이터 
for i in range(len(df2.index)):     # 모든 str -> int 변경
        for j in range(len(df2.iloc[i])):
                df2.iloc[i,j] = int(df2.iloc[i,j].replace(',', ''))  

df1 = df1.sort_values(['일자'], ascending=[True])
df2 = df2.sort_values(['일자'], ascending=[True])
print(df1)
print(df2)

df1 = df1.values
df2 = df2.values
print(type(df1), type(df2))
print(df1.shape, df2.shape)

np.save('data/kospi200.npy', arr=df1)
np.save('data/samsung.npy', arr=df2)