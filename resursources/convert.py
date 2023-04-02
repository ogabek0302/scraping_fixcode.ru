import pandas as pd

with open('fixcode.json', 'r') as f:
    data = pd.read_json(f)

data.to_excel('fixcode_excel.xlsx', index=False)
