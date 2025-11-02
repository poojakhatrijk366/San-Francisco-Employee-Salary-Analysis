# Project: San Francisco Employee Salary Analysis
# Author: Sushma J | Tool: Python (Pandas, Matplotlib, Seaborn)

# -----------------------------------------
# Import Libraries
# -----------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------------------
# Load Dataset
# -----------------------------------------
data = pd.read_csv("San_Francisco_Employee_Salaries.csv")

# Ensure graphs folder exists
if not os.path.exists("graphs"):
    os.makedirs("graphs")

# -----------------------------------------
# Data Overview
# -----------------------------------------
print("\nFirst 5 rows of the dataset:")
print(data.head())

print("\nColumn Names:")
print(data.columns.tolist())

# -----------------------------------------
# Convert Year to int (if not already)
# -----------------------------------------
data['Year'] = data['Year'].astype(int)

# -----------------------------------------
# 1️⃣ Average Total Pay Trend (2018–2024)
# -----------------------------------------
plt.figure(figsize=(8,5))
sns.lineplot(x='Year', y='Total_Pay', data=data, marker='o', color='blue')
plt.title("Average Total Pay Trend (2018–2024)")
plt.xlabel("Year")
plt.ylabel("Total Pay (USD)")
plt.tight_layout()
plt.savefig("graphs/1_pay_trend.png")
plt.close()

# -----------------------------------------
# 2️⃣ Top Job Titles by Average Base Pay
# -----------------------------------------
top_jobs = data.groupby('Job_Title')['Base_Pay'].mean().sort_values(ascending=False).head(5)
plt.figure(figsize=(8,5))
sns.barplot(x=top_jobs.values, y=top_jobs.index, palette="coolwarm")
plt.title("Top 5 Job Titles by Average Base Pay")
plt.xlabel("Average Base Pay (USD)")
plt.ylabel("Job Title")
plt.tight_layout()
plt.savefig("graphs/2_jobtitles_basepay.png")
plt.close()

# -----------------------------------------
# 3️⃣ Overtime vs Base Pay Comparison
# -----------------------------------------
plt.figure(figsize=(6,5))
sns.scatterplot(x='Base_Pay', y='Overtime_Pay', data=data, alpha=0.7, color='teal')
plt.title("Overtime Pay vs Base Pay")
plt.xlabel("Base Pay (USD)")
plt.ylabel("Overtime Pay (USD)")
plt.tight_layout()
plt.savefig("graphs/3_overtime_vs_basepay.png")
plt.close()

# -----------------------------------------
# 4️⃣ Pay Distribution by Department
# -----------------------------------------
dept_pay = data.groupby('Department')['Total_Pay_Benefits'].mean().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=dept_pay.values, y=dept_pay.index, palette="magma")
plt.title("Average Pay by Department")
plt.xlabel("Average Total Pay + Benefits (USD)")
plt.ylabel("Department")
plt.tight_layout()
plt.savefig("graphs/4_pay_by_department.png")
plt.close()

# -----------------------------------------
# 5️⃣ Summary Statistics
# -----------------------------------------
print("\nSummary Statistics:")
summary_cols = ['Base_Pay', 'Overtime_Pay', 'Total_Pay_Benefits']
print(data[summary_cols].describe().round(2))

# -----------------------------------------
# Completion Message
# -----------------------------------------
print("\n✅ Salary Analysis Completed! Graphs saved in the 'graphs' folder.")
print("✅ All tasks executed successfully!")