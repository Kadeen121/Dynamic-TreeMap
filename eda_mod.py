import pandas as pd 
import numpy as np

def df_eda(df):
    ''' This is  quick look at your data so you can begin your Exploratory Data Analysis.
    df: this is you DataFrame
    This is all you need to start very low code. 
    When you enter plug your DataFrame if the function
    you will get:
    The number of rows and colums in the DataFrame.
    The statistical shape of the data. 
    The number of nulls in each column.
    Each colums data type.
    A histogram to show the shape of the data'''
    rows,columns = df.shape
    describe = df.describe()
    nulls = df.isna().sum()[df.isna().sum()> 0]
    data_T = df.dtypes
    hist = df.hist(bins=60, figsize=(20,10))
    print(f'Rows:{rows}, Columns:{columns}\n\nNulls:\n{nulls}\n\nData Types:\n{data_T}\n\nTukey 5:\n{describe}')