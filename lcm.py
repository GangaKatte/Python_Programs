n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# Find the greater of the two numbers
if n1 > n2:
    greater = n1
else:
    greater = n2

while True:
    if (greater % n1 == 0) and (greater % n2 == 0):  # Check divisibility
        lcm = greater
        break  # Exit loop when LCM is found
    greater += 1  # Increment to check next number

print(f"LCM of {n1} and {n2} is {lcm}")
