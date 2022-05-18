import pandas as pd
import numpy as np

df = pd.read_csv("Victoria overflow basics all season.csv")
data_frame = pd.DataFrame(df[['Product', 'Variant','SALES SINCE MAY 2020']])

def overflow_stock(row):
    if (row['Stock'] > row['MAX STOCK ']):
        row['Overflow'] = row['Stock'] - row['MAX STOCK ']
    return row

df = df.apply(overflow_stock, axis=1)
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
df[['Product', 'Variant','Stock', 'Overflow']].to_csv('Basic_all_season overflow Victoria stock.csv')










#def fun_stock(row):
    #if (row['Stock'] > row['MAX STOCK ']):
        #row['Over'] = row['Stock'] - row['MAX STOCK ']
    #print(row)


#fun_stock(df)




