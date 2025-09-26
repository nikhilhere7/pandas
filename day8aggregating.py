# aggregating data meaning You have many rows,
# but you want to compress them into a single summary value.
# It’s basically group + summarize.
import pandas as pd 

df=pd.read_excel(r"C:\Users\nikhil mahale\Downloads\olympics-data(2).xlsx")
bois=pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")
# # value count 
print(df['born_city'].value_counts())

#astype
print(bois.dtypes["Units Sold"])
bois["Units Sold"]=bois["Units Sold"].astype(float)
print(bois.dtypes)

# # # groupby() and also sum()
print(bois.groupby(["Coffee Type"])["Units Sold"].sum())
# # mean()
print(bois.groupby(["Coffee Type"])["Units Sold"].mean())


# synatx 
# df.groupby("column").agg({"other_column": "function"})
# Where:
# groupby("column") → groups rows by that column.
# .agg({"other_column": "function"}) → applies a function like mean, sum, count, min, max.

# .agg()- count,max,min,mean,sum
# (so i have added price column in this )
bois["price"] = 4.99
print(bois.groupby(["Coffee Type"]).agg({"Units Sold":"sum" , "price":"mean"}))

# more ex of agg()
bois.groupby(['Coffee Type']).agg({'price':'min','Units Sold':'max'})

# to save any new column in database we can do (parmenet) and for just for now use (Loc)
bois=bois.to_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv" , index= False)
