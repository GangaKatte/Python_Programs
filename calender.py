import calendar  # Correct spelling

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)  # Correct usage
print(cal)
