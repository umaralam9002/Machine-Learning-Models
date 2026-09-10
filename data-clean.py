# ===============================
# Data Cleaning and Encoding
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# -------------------------------
# Step 1: Create Random Dataset
# -------------------------------

np.random.seed(42)

df = pd.DataFrame({
    "Age": np.random.randint(18, 60, 20).astype(float),
    "Salary": np.random.randint(30000, 100000, 20).astype(float),
    "Department": np.random.choice(["HR", "IT", "Sales", "Finance"], 20),
    "Gender": np.random.choice(["Male", "Female"], 20)
})

# Add Missing Values
df.loc[3, "Age"] = np.nan
df.loc[7, "Salary"] = np.nan
df.loc[5, "Department"] = np.nan
df.loc[10, "Gender"] = np.nan

# Add Outliers
df.loc[1, "Salary"] = 250000
df.loc[12, "Salary"] = 300000

print("========== Original Dataset ==========")
print(df)

# --------------------------------------
# Step 2: Handle Missing Numerical Values
# --------------------------------------

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# ---------------------------------------
# Step 3: Handle Missing Categorical Data
# ---------------------------------------

df["Department"].fillna(df["Department"].mode()[0], inplace=True)
df["Gender"].fillna(df["Gender"].mode()[0], inplace=True)

print("\n========== Dataset After Filling Missing Values ==========")
print(df)

# ----------------------------
# Step 4: Box Whisker Plot
# ----------------------------

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
sns.boxplot(y=df["Age"])
plt.title("Age Box Plot")

plt.subplot(1,2,2)
sns.boxplot(y=df["Salary"])
plt.title("Salary Box Plot")

plt.tight_layout()
plt.show()

# ----------------------------------------
# Step 5: Remove Outliers using IQR Method
# ----------------------------------------

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df[(df["Salary"] >= lower) & (df["Salary"] <= upper)]

print("\n========== Dataset After Removing Outliers ==========")
print(df_clean)

# ----------------------------
# Step 6: Label Encoding
# ----------------------------

label_df = df_clean.copy()

encoder = LabelEncoder()

label_df["Department"] = encoder.fit_transform(label_df["Department"])
label_df["Gender"] = encoder.fit_transform(label_df["Gender"])

print("\n========== Label Encoded Dataset ==========")
print(label_df)

# ----------------------------
# Step 7: One Hot Encoding
# ----------------------------

onehot_df = pd.get_dummies(
    df_clean,
    columns=["Department", "Gender"],
    drop_first=False
)

print("\n========== One Hot Encoded Dataset ==========")
print(onehot_df)
onehot_df = pd.get_dummies(
    df_clean,
    columns=["Department", "Gender"],
    dtype=int
)

print("\n========== One-Hot Encoded Dataset ==========")
print(onehot_df)
# ----------------------------
# Step 8: Histograms
# ----------------------------

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.hist(df_clean["Age"], bins=8, color="skyblue", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.subplot(1,2,2)
plt.hist(df_clean["Salary"], bins=8, color="orange", edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# ----------------------------
# Step 9: Correlation Heatmap
# ----------------------------

plt.figure(figsize=(6,4))
sns.heatmap(label_df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

print("\n========== Data Cleaning Completed Successfully ==========")

