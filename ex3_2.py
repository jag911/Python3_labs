import sys
var = input("Please enter a positive integer: ")
if var.isdecimal():
    num = int(var)
else:
    print("ERR: Non decimal value provided")
    sys.exit(1)

for value in range(num,-1,-2):
    print(f"{value}")