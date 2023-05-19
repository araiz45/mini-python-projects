import pandas as pd

# Read the Excel sheet
data = pd.read_excel('H:/shedule/16-May-2023.xlsx', sheet_name='Sheet1')

# Print the contents of the sheet
print(data)

data.at[4, "work"] = "Work"
print(data)
# data["work"] = ["break", "Play", "Enjoy", "Work", "Sleep"]
print(data)

data.to_excel('H:/shedule/16-May-2023.xlsx', index=False)
