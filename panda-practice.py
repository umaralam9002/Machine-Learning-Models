import pandas as pd

# --------------------------------------------------
# 1. Create the first dictionary and DataFrame
# --------------------------------------------------

Marks_data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha", "Umar"],
    "Marks": [85, 72, 91, 68, 88]
}

python_df = pd.DataFrame(Marks_data)

print("Python Marks DataFrame:")
print(python_df)


# --------------------------------------------------
# 2. Create the second dictionary and DataFrame
# --------------------------------------------------

database_marks_data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Database_Marks": [80, 75, 87, 70, 92]
}

database_df = pd.DataFrame(database_marks_data)

print("\nDatabase Marks DataFrame:")
print(database_df)


# --------------------------------------------------
# 3. Merge the two DataFrames
# --------------------------------------------------

# Student_ID is the common column in both DataFrames.
merged_df = pd.merge(
    python_df,
    database_df,
    on="Student_ID",
    how="inner"
)

print("\nMerged DataFrame:")
print(merged_df)


# --------------------------------------------------
# 4. Add calculated columns
# --------------------------------------------------

merged_df["Total_Marks"] = (
    merged_df["Marks"] +
    merged_df["Database_Marks"]
)

merged_df["Average_Marks"] = merged_df[
    ["Marks", "Database_Marks"]
].mean(axis=1)

# Assign grades using a custom function.
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "Fail"


merged_df["Grade"] = merged_df["Average_Marks"].apply(calculate_grade)

print("\nDataFrame After Calculations:")
print(merged_df)


# --------------------------------------------------
# 5. Basic DataFrame analysis
# --------------------------------------------------

print("\nFirst 3 Rows:")
print(merged_df.head(3))

print("\nLast 2 Rows:")
print(merged_df.tail(2))

print("\nDataFrame Shape:")
print(merged_df.shape)

print("\nColumn Names:")
print(merged_df.columns.tolist())

print("\nData Types:")
print(merged_df.dtypes)

print("\nStatistical Summary:")
print(merged_df.describe())

print("\nMissing Values:")
print(merged_df.isnull().sum())


# --------------------------------------------------
# 6. Statistical functions
# --------------------------------------------------

print("\nAverage Python Marks:")
print(merged_df["Marks"].mean())

print("\nHighest Database Marks:")
print(merged_df["Database_Marks"].max())

print("\nLowest Python Marks:")
print(merged_df["Marks"].min())

print("\nMedian Average Marks:")
print(merged_df["Average_Marks"].median())

print("\nStandard Deviation of Total Marks:")
print(merged_df["Total_Marks"].std())

print("\nSum of All Students' Total Marks:")
print(merged_df["Total_Marks"].sum())

print("\nNumber of Students:")
print(merged_df["Student_ID"].count())


# --------------------------------------------------
# 7. Find the top-performing student
# --------------------------------------------------

top_student = merged_df.loc[merged_df["Total_Marks"].idxmax()]

print("\nTop-Performing Student:")
print(top_student)


# --------------------------------------------------
# 8. Filter students
# --------------------------------------------------

high_scorers = merged_df[merged_df["Average_Marks"] >= 80]

print("\nStudents With Average Marks of 80 or Higher:")
print(high_scorers)


# --------------------------------------------------
# 9. Sort students by total marks
# --------------------------------------------------

sorted_df = merged_df.sort_values(
    by="Total_Marks",
    ascending=False
)

print("\nStudents Sorted by Total Marks:")
print(sorted_df)


# --------------------------------------------------
# 10. Group students by grade
# --------------------------------------------------

grade_counts = merged_df.groupby("Grade").size().reset_index(
    name="Number_of_Students"
)

print("\nNumber of Students in Each Grade:")
print(grade_counts)


# Calculate average marks for each grade.
grade_analysis = merged_df.groupby("Grade")[
    ["Marks", "Database_Marks", "Average_Marks"]
].mean().round(2)

print("\nAverage Marks Grouped by Grade:")
print(grade_analysis)


# --------------------------------------------------
# 11. Export DataFrames to CSV files
# --------------------------------------------------

python_df.to_csv("Marks.csv", index=False)
database_df.to_csv("database_marks.csv", index=False)
merged_df.to_csv("merged_student_results.csv", index=False)
sorted_df.to_csv("sorted_student_results.csv", index=False)

print("\nCSV files exported successfully.")


# --------------------------------------------------
# 12. Export DataFrames to one Excel workbook
# --------------------------------------------------

with pd.ExcelWriter(
    "student_results.xlsx",
    engine="openpyxl"
) as writer:
    python_df.to_excel(
        writer,
        sheet_name="Python Marks",
        index=False
    )

    database_df.to_excel(
        writer,
        sheet_name="Database Marks",
        index=False
    )

    merged_df.to_excel(
        writer,
        sheet_name="Merged Results",
        index=False
    )

    grade_counts.to_excel(
        writer,
        sheet_name="Grade Summary",
        index=False
    )

print("Excel workbook exported successfully.")
