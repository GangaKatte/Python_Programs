"""
*******
*** ***
**   **
*     *
**   **
*** ***
*******
"""
n = int(input("Enter : "))

# Top row
print("*" * (2 * n -1))

# Upper half
for i in range(1, n+1):
    print("*" * (n - i), " " * (2 * i - 1), "*" * (n - i), sep="")

# Lower half
for i in range(n - 1, 1, -1):
    print("*" * (n - i), " " * (2 * i - 1), "*" * (n - i), sep="")

# Bottom row
print("*" * (2 * n -1))
