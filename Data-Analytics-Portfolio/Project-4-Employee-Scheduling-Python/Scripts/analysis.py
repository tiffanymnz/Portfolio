import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
cleaned_data = pd.read_csv("cleaned_employee_data.csv")

# Workload Distribution by Department
avg_hours = cleaned_data.groupby("Department")["Hours_Worked"].mean()
avg_hours.plot(kind="bar", color="skyblue")
plt.title("Average Hours Worked by Department")
plt.xlabel("Department")
plt.ylabel("Average Hours Worked")
plt.savefig("avg_hours_department.png")
plt.show()

# Identify Employees with Excessive Overtime
excessive_overtime = cleaned_data[cleaned_data["Overtime_Hours"] > 10]
print("Employees with excessive overtime:")
print(excessive_overtime[["Employee_ID", "Department", "Overtime_Hours"]])

# Productivity Analysis
plt.scatter(cleaned_data["Hours_Worked"], cleaned_data["Tasks_Completed"], color="blue", alpha=0.6)
plt.title("Hours Worked vs Tasks Completed")
plt.xlabel("Hours Worked")
plt.ylabel("Tasks Completed")
plt.savefig("hours_vs_tasks.png")
plt.show()

plt.hist(cleaned_data["Efficiency_Rating"], bins=10, color="green", edgecolor="black")
plt.title("Efficiency Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.savefig("efficiency_distribution.png")
plt.show()
