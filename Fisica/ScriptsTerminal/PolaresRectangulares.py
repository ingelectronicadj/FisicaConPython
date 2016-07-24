#CONVERTIR DE POLARES A RECTANGULARES
from math import sin,cos,pi

# Ask the user for the values of r and theta
r = float(input("Ingresa magnitud r: "))
d = float(input("Ingresa angulo en grados: "))

# Convert the angle to radians
theta = d*pi/180

# Calculate the equivalent Cartesian coordinates
x = r*cos(theta)
y = r*sin(theta)

# Print out the results
print("x = ",x,", y = ",y)