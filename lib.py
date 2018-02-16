import pandas as pd
import numpy as np
import matplotlib as plt
url="http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv(url, header=None)

print(df)

headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compressionratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
print(headers)

df.columns=headers
   
    
q=df.head(10)
print(q)

s=df.tail(10)
print(s)

type=df.dtypes
print(type)

ds=df.describe(include="all")
print(ds)

a=df["symboling"]
print(a)

b=df["make"]
print(b)

c=df["fuel-type"]
print(c)
drp=df.dropna(subset=["price"],axis=0,inplace=True)
print(drp)
