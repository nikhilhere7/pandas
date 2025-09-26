import pandas as pd 

df=pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")

# to add a column 
df["price"] = 4.99
print(df.head())
# # ex
df["chief"] = "nikhil"
print(df.head())
# # to remove , mentioned "drop"
# # to drop any column 
print(df.drop(columns=["Day"]))
# # tp drop any keyword 
print(df.drop(0))
# update any row 
df.loc[df["Day"]=="monday", "CoffeeType"]= "latte"
print(df.loc[df["Day"]=="monday"])

# to rename any column 
print(df.rename(columns={"Day":"day"}))
#  i have done for multiply 
print(df.rename(columns={"Day":"day","Coffee Type":"coffee type"}))
