# Quadratic Equation using Function Decomposition

def calculate_discriminant(a,b,c):
    return b * b - 4 * a * c

def calculate_roots(a,b,d):
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)

    if x1 == x2:
        print("x= ", x1)
    else:
        print("x1= ", x1)
        print("x2= ", x2)

def main(a,b,c):
    discriminant = calculate_discriminant(a,b,c)
    if discriminant < 0:
        print("No real roots! ")
    else:
        calculate_roots(a, b, discriminant)

a = int(input("Enter the coefficient of a: "))
b = int(input("Enter the coefficient of b: "))
c = int(input("Enter the coefficient of c: "))

main(a,b,c)