def add(*args):
    total = 0
    for num in args:
        total += num
    return total

def sub(x,z):
    return float(x - z)

def mul(*args):
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x,z):
    return round(x/z,3)

print("**** BASIC CALC ****")

print(f"4+3 = {add(4,3)}")
print(f"4+3+2+1 = {add(4,3,2,1)}")

print(f"4*3 = {mul(4,3)}")
print(f"4*3*2 = {mul(4,3,2)}")

print(f"4-3 = {sub(4,3)}")

print(f"4/3 = {div(4,3)}")
