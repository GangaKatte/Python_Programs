"""
   A
  ABA
 ABCBA 
"""

n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    # Print leading spaces
    print(" " * (n - i), end="")

    # Print increasing characters (A, B, C, ...)
    for j in range(1, i+1):
        print(chr(65 + j - 1), end="")

    # Print decreasing characters (B, A, ...)
    for j in range(i-1, 0, -1):
        print(chr(65 + j - 1), end="")

    print()  # Move to the next line
