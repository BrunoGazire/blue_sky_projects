import pandas as pd
df = pd.read_csv("Victoria Overflow.csv")
data_frame = pd.DataFrame(df[['Product','Variant','MAX STOCK ','Stock']])

#Function to retrive overflow products and qnty

def fun_stock(row):
    if(row['Stock'] > row['MAX STOCK ']):
        row['RETURN TO WAREHOUSE'] = row['Stock'] - row['MAX STOCK ']
    return row
df = df.apply(fun_stock, axis = 1)
df.dropna(inplace = True)
df.reset_index(drop=True, inplace = True)

#Export to csv file 

df[['Product', 'Variant','Stock', 'RETURN TO WAREHOUSE']].to_csv('stock_overflow_Victoria.csv')
















