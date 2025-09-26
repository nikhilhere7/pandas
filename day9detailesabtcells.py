# 1.Parentheses ()
#     👉 Used for functions/method calls.
#     df.head(10)           # function call with argument
#     df.groupby("team")    # calling groupby method
#     df["points"].mean()   # mean() is a function call

# 2.Square Brackets []
#     👉 Used for indexing / selecting.
#     df["points"]             # single column (Series)
#     df[["points", "team"]]   # multiple columns (DataFrame)
#     f you’re inside [], you’re asking Pandas: “which rows/columns?”

# 3.Curly Braces {}
#     👉 Used for dictionaries, mainly in operations like agg, rename, etc.
#     df.groupby("team").agg({
#         "points": "mean",
#         "assists": "sum"
#     })
#     You never use {} for indexing rows/columns. 
#     It’s only when Pandas expects a mapping/dictionary.

# Mnemonic (to never forget)

# () → do something (call a method).

# [] → get something (rows/columns).

# {} → map something (dict-style instructions).