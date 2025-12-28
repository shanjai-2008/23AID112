a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if a > b:
    print("First number is bigger")
elif b > a:
    print("Second number is bigger")
else:
    print("Both numbers are equal")

