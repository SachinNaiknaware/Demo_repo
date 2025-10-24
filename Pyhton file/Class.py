### class 

import pandas as pd

file_path = '/home/sachin/Downloads/archive2/Activity_tracking_sheet.csv'

# Try reading with ISO-8859-1 encoding (also known as Latin-1)
df = pd.read_csv(file_path, encoding='ISO-8859-1')

#print(df.head())
print(df.columns())
