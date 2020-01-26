#! /usr/bin/env python3

# Anthony Moore
# Calculate the square root of a number

def sqrt(x):
    """
    Calculate square root of x
    """
    # Check that x is positive
    if x < 0:
        print("Error: Invalid Number")
        return -1
    else:
        print("Correct number")
    

    # initial guess value of sqrt
    z = x / 2

    # continiously improve guess
    # adapted from https://tour.golang.org/flowcontrol/8
    while abs(x - (z*z)) > 0.00001:
        z -= (z * z - x) / (2 * z)

    return z

value = 63.0

print("The Square root of", value, "is: ",  sqrt(value))

