import pandas as pd
xl = pd.ExcelFile("assets/test.xlsx")
xl.sheet_names
df = xl.parse("List1")
print(df.head())