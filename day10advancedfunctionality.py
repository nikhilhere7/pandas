# advanced functionaity - shift(), rank(),rolling(),cumsum()
# .shift()- so basically it shifty the data to next and fornt
import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")
boys=pd.read_excel(r"C:\Users\nikhil mahale\Downloads\olympics-data(2).xlsx")

def revenue(coffee):
    if coffee == "Espresso":
        return 120
    elif coffee == "Latte":
        return 130
    else:
        "invalid"

df["Revenue"]=df["Coffee Type"].apply(revenue)

df.to_csv("coffee_with_revenue.csv", index=False)
# # .shift()- so basically it shifty the data to next and fornt
df["yesterday_revenue"] = df["Revenue"].shift(1)
print(df.head())
# .rank()
boys['height_rank']=boys['height_cm'].rank()
print(boys.head())