import pandas as pd
import matplotlib.pyplot as plt

# Read employee data
df = pd.read_csv("employees.csv")

# Calculate average salary department-wise
avg_salary = df.groupby("department")["salary"].mean()

# Create bar chart
plt.bar(avg_salary.index, avg_salary.values, color="skyblue")

# Add title and labels
plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Display values on bars
for i, value in enumerate(avg_salary.values):
    plt.text(i, value, str(round(value, 2)), ha="center")

# Save chart
plt.savefig("bar_chart.png")

# Display chart
plt.show()

# Histogram of employee salaries

plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5, color="orange", edgecolor="black")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.savefig("histogram.png")

plt.show()

# Chart 3 - Scatter Plot

plt.figure(figsize=(8, 5))

for department in df["department"].unique():
    data = df[df["department"] == department]

    plt.scatter(data["id"], data["salary"], label=department)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")

plt.legend(title="Department")

plt.savefig("scatter_plot.png")

plt.show()

# Chart 4 - Monthly Sales Line Chart

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(months, sales, marker="o", color="green",
         label="Monthly Sales")

plt.title("Monthly Sales (Jan to Jun)")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.grid(True)

plt.savefig("line_chart.png")

plt.show()

# Bonus Challenge - 4 charts in one figure

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# Chart 1 - Bar chart
avg_salary = df.groupby("department")["salary"].mean()

ax[0, 0].bar(avg_salary.index, avg_salary.values)
ax[0, 0].set_title("Average Salary by Department")
ax[0, 0].set_xlabel("Department")
ax[0, 0].set_ylabel("Average Salary")

# Chart 2 - Histogram
ax[0, 1].hist(df["salary"], bins=5, color="orange",
              edgecolor="black")
ax[0, 1].set_title("Salary Histogram")
ax[0, 1].set_xlabel("Salary")
ax[0, 1].set_ylabel("Employees")

# Chart 3 - Scatter plot
for department in df["department"].unique():
    data = df[df["department"] == department]
    ax[1, 0].scatter(data["id"], data["salary"],
                      label=department)

ax[1, 0].set_title("ID vs Salary")
ax[1, 0].set_xlabel("Employee ID")
ax[1, 0].set_ylabel("Salary")
ax[1, 0].legend()

# Chart 4 - Line chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

ax[1, 1].plot(months, sales, marker="o")
ax[1, 1].set_title("Monthly Sales")
ax[1, 1].set_xlabel("Month")
ax[1, 1].set_ylabel("Sales")

plt.tight_layout()

plt.savefig("all_charts.png")

plt.show()





