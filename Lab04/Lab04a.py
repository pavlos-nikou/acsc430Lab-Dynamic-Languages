from math import pi, sqrt
from Lab04b import *


def cone_surface_area(r,h):
    return pi * r**2 + pi * r * sqrt(r**2 + h**2)

def cone_volume(r,h):
    return pi * r**2 * h/3
    
# Print out a message indicating what the program does.
print("Welcome")
print("This program prompts the user for the radius and height of a 3-dimensional cone")
print("and then calculates and prints the surface area and volume of the cone.\n")

# Prompt the user for the radius (a non-negative float) in feet.
radius = get_nneg_float("please provide the radius (in feet) of the desired cone:  ")
# Prompt the user for the height (a non-negative float) in feet.
height = get_nneg_float("please provide the height (in feet) of the desired cone:  ")

# Print the radius and height, but rounded to 2 decimal digits
print(f'Radius: {radius:.2f}\tHeight: {height:.2f}')

# Print the surface area and volume rounded to 2 decimal digits.
print(f'the Surface Area of the cone is : {cone_surface_area(radius,height):.2f} square feet')
print(f'the Volume of the cone is : {cone_volume(radius,height):.2f} cubic feet')
