import sys
value_in = input("Please enter a year: ")
if len(value_in) != 4 or not value_in.isdecimal():
    print("Invalid Year Provided")
    sys.exit(1)

year = int(value_in)
if (year%4 == 0 and (year%100 != 0 or year%400 == 0)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT aleap year")

sys.exit(0)