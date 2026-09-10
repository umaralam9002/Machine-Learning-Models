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