name = "Umar"
age = 25

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1} years old.")

print("-----------------------------")

name = input("Enter your name: ")
print(f"Welcome, {name}!")

print("-----------------------------")

def greet(name):
    return f"Hello, {name}! Welcome to Python."

user = input("Enter your name: ")
print(greet(user))


print("-----------------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero.")

