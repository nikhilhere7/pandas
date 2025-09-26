# will learn abt groupby()
import pandas as pd 

df=pd.read_excel(r"C:\Users\nikhil mahale\Downloads\olympics-data(2).xlsx")

# df.groupby("column").agg({"other_column": "function"})
# Where:
# groupby("column") → groups rows by that column.
# ex of agg()
# print(df.groupby(['name']).agg({'height_cm':'mean','weight_kg':'sum'}))
# # to group any perticular column 
# print(df.groupby(['name']))

# transform-transform means “apply a function to each group, 
# but return the result aligned with the original DataFrame shape
# groupby().mean() = collapse → fewer rows.
# groupby().transform("mean") = broadcast → same number of rows, with group-level stat per row.
# df=df.groupby(['name'])['height_cm'].transform('mean')
# print(df.head())

# Advanced Powers
# Multi-index results
# When grouping by multiple columns:
df=df.groupby(['name','born_city'])['weight_kg'].mean()
print(df.head)
