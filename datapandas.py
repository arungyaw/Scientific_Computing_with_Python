import pandas as pd

#Creating a DataFrame

df = pd.DataFrame({
    'Study_Hours': [5,2,7,1,9],
    'Sleep_Hours' : [8,10,6,7,5],
    'Passed' : [1,0,1,0,1]
})

print(df.head())
print(df.describe())
