import math

# Input coefficients
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate discriminant
d = b*b - 4*a*c

# Find roots
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are real and different")
    print("Root 1 =", r1)
    print("Root 2 =", r2)

elif d == 0:
    r = -b / (2*a)
    print("Roots are real and equal")
    print("Root =", r)

else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Roots are complex")
    print("Root 1 =", real, "+", imag, "i")
    print("Root 2 =", real, "-", imag, "i")