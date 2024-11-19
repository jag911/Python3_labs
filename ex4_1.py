#! /usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print('-'*len(Belgium))
print(Belgium.replace(",",":"))
bel_pop = int(Belgium.split(",")[1])
cap_pop = int(Belgium.split(",")[3])

total = bel_pop + cap_pop
print(total)
print('-'*len(Belgium))
