'''
Convert an Excel file into a CSV file using Python 
'''

import pandas as pd

# Read Excel file
data = pd.read_excel("sample.xlsx")

#Convert to CSV
data.to_csv("output.csv", index=False)

print("Excel file successfully converted to CSV!")