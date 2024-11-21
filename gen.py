import decimal

def frange(start,stop=None,step=.25):
    if step == 0: return None
    if stop == None:
        i = float(0)
        j = float(start)
    elif start >= stop:
        return None
    else:
        i = float(start)
        j = float(stop)
    i = decimal.Decimal(str(i))
    j = decimal.Decimal(str(j))
    step = decimal.Decimal(str(step))
    while i < j:
        yield(float(i))
        i += step


print(list(frange(1.1,3)))
print(list(frange(1,3, 0.33)))
print(list(frange(1,3,1)))
print(list(frange(3,1)))
print(list(frange(1,3,0)))
print(list(frange(-1,-.05,0.1)))

alist = []
for num in frange(3.142, 12):
    alist.append(num)
print(list(alist))
print(frange(1,2))

print(list(frange(3)))