import pandas as pd 

df=pd.read_excel(r"C:\Users\nikhil mahale\Downloads\olympics-data(2).xlsx")
# first method 
print(df.loc[df["height_cm"] > 215, ["name", "height_cm"]])
# second method
print(df[df["height_cm"] > 215][["name","height_cm"]])
# now filtering with two parameters 
print(df[(df["height_cm"] > 215) & (df["born_country"] == "USA")])
# for specified keywords 
print(df[df["name"]=="Shaquille O'Neal"])
# to find any keyword within name like contain str is string 
print(df[df["name"].str.contains("Keith")])

# and(&)
df[(df["height_cm"] > 215) & (df["born_country"] == "USA")]
# or(|)
df[(df["height_cm"] > 215) | (df["born_country"] == "USA")]
# not(~)
df[~(df["height_cm"] > 215)]
# operations with strings
df[df["name"].str.contains("Michael")]
df[df["born_city"].str.startswith("San")]
df[df["born_city"].str.endswith("burg")]
# filter by various inputs 
df[df["born_country"].isin(["USA", "GER", "BRA"])]

