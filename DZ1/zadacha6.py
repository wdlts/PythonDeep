try:
    year = int(input("Input year: "))
    print("Leap year" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "Not a leap year")
except ValueError:
    print("This is not a number")


