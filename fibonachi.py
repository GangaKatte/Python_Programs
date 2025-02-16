# Python program to generate Fibonacci series up to n terms

n = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

print("Fibonacci Sequence:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Update values
