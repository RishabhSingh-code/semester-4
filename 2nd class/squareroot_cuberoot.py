a = int(input("Enter your first number = "))
b = int(input("Enter your second number = "))
c = a * b

print(f"Product: {c}")

# Check odd/even
if c % 2 != 0:
    square = c**2
    print("Square of the product =", square)
elif c % 2 == 0:
    cube = c**3
    print("Cube of the product =", cube)

# Check range
if c > 50 and c < 200:
    squareroot = c**(1/2)
    print("Square root of the product =", squareroot)
elif c > 200:
    cuberoot = c**(1/3)
    print("Cube root of the product =", cuberoot)
