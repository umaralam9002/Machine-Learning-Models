

import numpy as np

student_name = "Muhammad Umar Alam"
course_name = "Python Programming"



print("Student Name:", student_name)
print("Course Name:", course_name)


print("Length of name:", len(student_name))


print("Uppercase:", student_name.upper())
print("Lowercase:", student_name.lower())


print("First character:", student_name[0])
print("Last character:", student_name[-1])

# String slicing
print("First 8 characters:", student_name[0:8])

# Replace part of a string
updated_course = course_name.replace("Python", "Advanced Python")
print("Updated course:", updated_course)

# Check whether text exists inside a string
if "Umar" in student_name:
    print("Umar exists in the student's name.")

# Split a string into a list
name_parts = student_name.split()
print("Name parts:", name_parts)

# Loop through the words in a string
print("\nWords in the student's name:")

for word in name_parts:
    print(word)


# ==================================================
# 2. LISTS AS PYTHON ARRAYS
# ==================================================

# Python normally uses lists as basic arrays.
marks = [85, 72, 91, 68, 88]
marks2 = [110,220,330,440]

print("\n===== PYTHON LIST/ARRAY OPERATIONS =====")

print("All marks:", marks)
print("First mark:", marks[0])
print("Last mark:", marks[-1])

# Add an item
marks.append(95)
print("After adding a mark:", marks)

# Update an item
marks[1] = 75
print("After updating the second mark:", marks)

# Remove an item
marks.remove(68)
print("After removing 68:", marks)

# Sort in ascending order
marks.sort()
print("Marks in ascending order:", marks)

# Useful array functions
print("Number of marks:", len(marks))
print("Total marks:", sum(marks))
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Average marks:", sum(marks) / len(marks))


# ==================================================
# 3. RANGE FUNCTION
# ==================================================

print("\n===== RANGE EXAMPLES =====")

# range(stop)
print("Numbers from 0 to 4:")

for number in range(5):
    print(number)

# range(start, stop)
print("\nNumbers from 1 to 5:")

for number in range(1, 6):
    print(number)

# range(start, stop, step)
print("\nEven numbers from 2 to 10:")

for number in range(2, 11, 2):
    print(number)

# Reverse range
print("\nCountdown:")

for number in range(5, 0, -1):
    print(number)

print("Finished!")


# ==================================================
# 4. FOR LOOPS
# ==================================================

student_names = ["Ali", "Ahmed", "Sara", "Ayesha", "Umar"]
student_marks = [85, 72, 91, 68, 88]

print("\n===== FOR LOOP =====")

for name in student_names:
    print("Student:", name)

# Use index with range()
print("\nStudents and marks:")

for index in range(len(student_names)):
    print(
        student_names[index],
        "scored",
        student_marks[index]
    )

# A cleaner way using zip()
print("\nUsing zip:")

for name, mark in zip(student_names, student_marks):
    print(f"{name} scored {mark} marks.")


# ==================================================
# 5. IF CONDITIONS INSIDE A LOOP
# ==================================================

print("\n===== CONDITIONS INSIDE A LOOP =====")

for name, mark in zip(student_names, student_marks):

    if mark >= 80:
        result = "Excellent"

    elif mark >= 70:
        result = "Good"

    elif mark >= 60:
        result = "Pass"

    else:
        result = "Fail"

    print(f"{name}: {mark} marks - {result}")


# ==================================================
# 6. WHILE LOOP
# ==================================================

print("\n===== WHILE LOOP =====")

counter = 1

while counter <= 5:
    print("Counter value:", counter)
    counter += 1


# ==================================================
# 7. BREAK AND CONTINUE
# ==================================================

print("\n===== BREAK EXAMPLE =====")

for number in range(1, 11):

    if number == 6:
        break

    print(number)

print("\n===== CONTINUE EXAMPLE =====")

for number in range(1, 11):

    # Skip even numbers
    if number % 2 == 0:
        continue

    print(number)


# ==================================================
# 8. NESTED LOOPS
# ==================================================

print("\n===== MULTIPLICATION TABLE =====")

for row in range(1, 4):

    for column in range(1, 6):
        print(
            row,
            "x",
            column,
            "=",
            row * column
        )

    print()


# ==================================================
# 9. TWO-DIMENSIONAL ARRAY
# ==================================================

marks_matrix = [
    [85, 80],
    [72, 75],
    [91, 87],
    [68, 70],
    [88, 92]
]

print("\n===== TWO-DIMENSIONAL ARRAY =====")

print("Complete matrix:", marks_matrix)
print("First row:", marks_matrix[0])
print("First value:", marks_matrix[0][0])

print("\nValues in the matrix:")

for row in marks_matrix:
    for value in row:
        print(value, end=" ")

    print()


# ==================================================
# 10. MANUAL MATRIX MULTIPLICATION
# ==================================================

matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

# Create an empty result matrix containing zeros.
result_matrix = [
    [0, 0],
    [0, 0]
]

print("\n===== MANUAL MATRIX MULTIPLICATION =====")

# Rows of matrix A
for row in range(len(matrix_a)):

    # Columns of matrix B
    for column in range(len(matrix_b[0])):

        # Elements in the selected row and column
        for item in range(len(matrix_b)):
            result_matrix[row][column] += (
                matrix_a[row][item]
                * matrix_b[item][column]
            )

print("Matrix A:")
for row in matrix_a:
    print(row)

print("Matrix B:")
for row in matrix_b:
    print(row)

print("Multiplication result:")
for row in result_matrix:
    print(row)


# ==================================================
# 11. MATRIX MULTIPLICATION USING NUMPY
# ==================================================

numpy_matrix_a = np.array([
    [1, 2],
    [3, 4]
])

numpy_matrix_b = np.array([
    [5, 6],
    [7, 8]
])

print("\n===== NUMPY MATRIX MULTIPLICATION =====")

print("NumPy Matrix A:")
print(numpy_matrix_a)

print("\nNumPy Matrix B:")
print(numpy_matrix_b)

# Method 1: @ operator
numpy_result_1 = numpy_matrix_a @ numpy_matrix_b

print("\nResult using @ operator:")
print(numpy_result_1)

# Method 2: np.matmul()
numpy_result_2 = np.matmul(
    numpy_matrix_a,
    numpy_matrix_b
)

print("\nResult using np.matmul():")
print(numpy_result_2)

# Method 3: np.dot()
numpy_result_3 = np.dot(
    numpy_matrix_a,
    numpy_matrix_b
)

print("\nResult using np.dot():")
print(numpy_result_3)


# ==================================================
# 12. OTHER NUMPY ARRAY OPERATIONS
# ==================================================

numbers = np.array([10, 20, 30, 40, 50])

print("\n===== NUMPY ARRAY ANALYSIS =====")

print("Array:", numbers)
print("Array size:", numbers.size)
print("Array shape:", numbers.shape)
print("Sum:", numbers.sum())
print("Mean:", numbers.mean())
print("Maximum:", numbers.max())
print("Minimum:", numbers.min())

# Multiply every element by 2
print("Array multiplied by 2:")
print(numbers * 2)

# Select values greater than 25
print("Values greater than 25:")
print(numbers[numbers > 25])