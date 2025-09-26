import pandas as pd 

df=pd.read_excel(r"C:\Users\nikhil mahale\Downloads\olympics-data(2).xlsx")

def categorize(row):
    if (row["height_cm"] < 175) and (row["weight_kg"] < 70):
        return "lightweight"
    else:
        return "overweight"
df["categories"]=df.apply(categorize , axis=1 )
print(df.head())

# practice 
# def xyz(row):
#     if (row["height_cm"] < 60) & (row["weight_kg"] < 70 ):
#         return "lightweight"
#     else:
#         return"overweight"
# df["categories"]=df.apply(xyz , axis=1 )
# print(df.head())