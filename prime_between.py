# Python program to display all prime numbers within an interval
lower = 1
upper = 10

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    # All prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:  # This else belongs to the for-loop, not the if
            print(num)
