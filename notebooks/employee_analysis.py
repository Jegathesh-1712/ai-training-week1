#!/usr/bin/env python
# coding: utf-8

# # Week 1 - Day 4
# ## Task 2 - Employee Data Analysis
# ### Data Loading and Exploration

# In[35]:


import pandas as pd
from pathlib import Path

# Load employee dataset
file_path = Path("../data/employees.csv")

df = pd.read_csv(file_path)

# Display first five rows
print("First 5 Employee Records:")
display(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())


# In[36]:


# Dataset information
print("Dataset Information:")
df.info()

# Statistical summary
print("\nStatistical Summary:")
display(df.describe())

# Dataset dimensions
print("\nNumber of Rows and Columns:")
print(df.shape)


# In[37]:


# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())


# In[38]:


# Employee count by department
print("Employees by Department:")
display(df["department"].value_counts())

# Average salary by department
print("\nAverage Salary by Department:")
display(df.groupby("department")["salary"].mean())


# In[39]:


print("Employees by City:")
display(df["city"].value_counts())

print("\nAverage Salary:")
print(df["salary"].mean())

print("\nHighest Salary:")
print(df["salary"].max())

print("\nLowest Salary:")
print(df["salary"].min())


# In[40]:


# Check missing values
print("Missing Values:")
display(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Check data types
print("\nColumn Data Types:")
print(df.dtypes)


# ## Five Business Questions
# 
# 1. Which department has the highest number of employees?
# 2. Which department offers the highest average salary?
# 3. Which city has the highest number of employees?
# 4. Who is the highest-paid employee?
# 5. What is the average salary of all employees?

# In[41]:


# 1. Department with most employees
print("Employees by Department:")
display(df["department"].value_counts())

# 2. Department with highest average salary
print("\nAverage Salary by Department:")
display(df.groupby("department")["salary"].mean())

# 3. City with most employees
print("\nEmployees by City:")
display(df["city"].value_counts())

# 4. Highest-paid employee
print("\nHighest Paid Employee:")
display(df.loc[df["salary"].idxmax()])

# 5. Overall average salary
print("\nOverall Average Salary:")
print(df["salary"].mean())


# ## Data Dictionary
# 
# | Column | Description | Data Type |
# |---|---|---|
# | id | Unique employee ID | Integer |
# | name | Employee name | String |
# | department | Employee department | String |
# | salary | Employee salary | Integer |
# | city | Employee city | String |
