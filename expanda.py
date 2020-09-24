import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_excel('example.xlsx')

#df["col"] = df["teste"]-25772305
df["col"]= df["teste"]/29441332*100


#pivot = pd.pivot_table(df, index='teste')


#pivot['% of column total'] = (pivot['teste']/177466715)*100

print(df["col"])
