import numpy as np

matrix_a = [[1,2],[3,4]]

matrix_b = [[5,6,7], [8,9,10]]


result_matrix = [[0,0,0],[0,0,0]]


for rows in range(len(matrix_a)):

    for colum in range(len(matrix_b[0])):

        for item in range (len(matrix_b)):

            result_matrix[rows][colum] += (matrix_a[rows][item] * matrix_b[item][colum]) 


print(result_matrix)

print("------------------------")

numpy_matrix_a = np.array([[1,2],[3,4]])
numpy_matrix_b = np.array([[5,6],[7,8]])

numpy_result_2 = np.matmul(
    numpy_matrix_a,
    numpy_matrix_b
)

print("\nResult using np.matmul():")
print(numpy_result_2)

print("--------------------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Modulus:", num1 % num2)
else:
    print("Division and Modulus not possible because the second number is 0.")

print("Exponentiation:", num1 ** num2)


print("------------------------------------")

numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("Array size:", numbers.size)
print("Array shape:", numbers.shape)
print("Sum:", numbers.sum())
print("Mean:", numbers.mean())
print("Maximum:", numbers.max())
print("Minimum:", numbers.min())
print("Array multiplied by 2:")
print(numbers * 2)
print("Values greater than 25:")
print(numbers[numbers > 25])



print("-----------------------------------")

print("Linear Equation")

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

if a != 0:
    x = (c - b) / a
    print("Value of x:", x)
else:
    print("Equation cannot be solved.")




print("---------------------------------")


print("Quadratic Equation")

import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Two solutions:")
    print("x1 =", x1)
    print("x2 =", x2)

elif discriminant == 0:
    x = -b / (2 * a)
    print("One solution:")
    print("x =", x)

else:
    print("No real solutions.")
