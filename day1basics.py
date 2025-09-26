import pandas as pd 

df=pd.DataFrame(((1,2,3,4),(5,6,7,8),(9,10,11,12)),
                columns=("a","b","c","d"),
                index=("x","y","z"))

# print(df.head())
# print(df.info())
# print(df.describe())
# if we want to access specified line then
print(df.loc(1))
