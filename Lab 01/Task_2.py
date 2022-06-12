import math

print('Enter the radius of a circle:')
radius = int(input())

circumference = 2 * math.pi * radius

print("The circumference of the circle is", circumference)

if radius % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')
