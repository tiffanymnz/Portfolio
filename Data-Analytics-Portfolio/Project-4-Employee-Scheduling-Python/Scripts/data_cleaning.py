import pandas as pd

# Load raw data
data = pd.read_csv("employee_data.csv")

# Remove duplicate rows
data = data.drop_duplicates()

# Standardize department names
data["Department"] = data["Department"].str.strip().str.title()

# Replace invalid values
data["Overtime_Hours"] = data["Overtime_Hours"].apply(lambda x: x if x >= 0 else None)

# Fill missing values
data["Hours_Worked"] = data["Hours_Worked"].fillna(data["Hours_Worked"].median())
data["Tasks_Completed"] = data["Tasks_Completed"].fillna(data["Tasks_Completed"].median())
data["Overtime_Hours"] = data["Overtime_Hours"].fillna(0)
data["Efficiency_Rating"] = data["Efficiency_Rating"].fillna(data["Efficiency_Rating"].mean())

# Save cleaned data
data.to_csv("cleaned_employee_data.csv", index=False)
print("Data cleaned and saved!")
