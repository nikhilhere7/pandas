#merging and concatentaion data 

# Merging in Pandas

# Think of merge like SQL joins: you combine two tables based on a common column (a "key").
# Here, the common key is athlete_id (present in both bios and results).
# # ex
import pandas as pd
df=0
df_results=0
merged = pd.merge(df, df_results, on="athlete_id", how="inner")
print(merged.head())

# What happens:

# Pandas takes every row from bios and matches it with rows from results where athlete_id matches.
# So now, one big DataFrame will have name, age, country, medal, event, etc. in one row.

# Types of Joins

# how="inner" → only keep matching rows.
# how="left" → keep all rows from bios (left table), even if no match in results.
# how="right" → keep all rows from results (right table).
# how="outer" → keep everything from both, fill blanks with NaN.

# 💡 Memory trick:

# Inner = intersection
# Left/Right = direction
# Outer = union
