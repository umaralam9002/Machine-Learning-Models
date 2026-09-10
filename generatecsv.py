import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

n = 500

names = [f"Student_{i}" for i in range(1, n + 1)]

genders = ["Male", "Female"]

departments = ["Computer Science", "Business", "Engineering", "Mathematics", "Arts"]

grades = ["Poor", "Average", "Good", "Excellent"]  # Ordinal

cities = ["New York", "Chicago", "Houston", "Boston", "Dallas", "Seattle"]

data = pd.DataFrame({
    "Student_ID": range(1001, 1001+n),
    "Name": names,
    "Age": np.random.randint(17, 30, n),
    "Gender": np.random.choice(genders, n),
    "Department": np.random.choice(departments, n),
    "Grade": np.random.choice(grades, n),
    "Attendance": np.random.randint(50, 101, n),
    "Marks": np.random.randint(35, 101, n),
    "City": np.random.choice(cities, n),
    "Study_Hours": np.round(np.random.normal(4, 1.5, n), 1)
})

# -------------------------
# Add Missing Values
# -------------------------

for col in ["Age", "Gender", "Department", "Grade",
            "Attendance", "Marks", "City", "Study_Hours"]:
    idx = np.random.choice(data.index, 20, replace=False)
    data.loc[idx, col] = np.nan

# -------------------------
# Add Outliers
# -------------------------

outliers = np.random.choice(data.index, 8, replace=False)

data.loc[outliers[:4], "Marks"] = [150, 180, 200, 170]

data.loc[outliers[4:], "Study_Hours"] = [15, 18, 20, 16]

# -------------------------
# Add Duplicate Rows
# -------------------------

duplicates = data.sample(10, random_state=1)

data = pd.concat([data, duplicates], ignore_index=True)

# Keep exactly 500 rows
data = data.iloc[:500]

# -------------------------
# Shuffle Dataset
# -------------------------

data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# -------------------------
# Save CSV
# -------------------------

data.to_csv("student_data.csv", index=False)

print("CSV file created successfully!")
print(data.head())
