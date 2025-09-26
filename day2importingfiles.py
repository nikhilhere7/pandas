import pandas as pd 
# this is the fastest method but take more space 
coffee=pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")
# syntax 
# print(coffee.iloc[#row,#cloumn])
# this is for entire rows (0,1,2)
print(coffee.iloc[[0, 1, 2]])
# if you want a specific cell (row 2, column 1)
print(coffee.iloc[2,1])
# this is for in one row multiply column 
print(coffee.iloc[2,[0,1,2]])
# and then you can use this method which is slow but take less space 
result=pd.read_parquet("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")

print(result.head())
# id why this parquet is not working , still we have this to method 
# (for excel we use "pd.read.excel")

# to update any row we have this
print(coffee.iloc[1,"units sold"]) = 10
