from math import pi, tan, cos

height = 1
distance = 0.5
elevation = 80
velocity = 44
theta = elevation * (pi/180)
y = height + (distance * tan(theta)) - ((9.8 * (velocity**2)) / (2 * (velocity * cos(theta)**2)))
print(y)