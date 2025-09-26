import pandas as pd 
coffee=pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")
# we can get specified columns 
print(coffee["Day"])
# for sorting out 
print(coffee.sort_values("Units Sold"))
# for decending order go for this 
print(coffee.sort_values("Units Sold",ascending=False))

