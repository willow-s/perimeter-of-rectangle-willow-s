# Willow Skagos, CS 20, October 10 2019, This program will calculate
# the perimeter of a rectangle


def perimeter_rect(b, h):
    """This function will find the perimeter, P, of a rectangle
    with base, b, and height, h"""
    # this is the formula to find the perimeter of the rectangle
    P = (2 * b) + (2 * h)
    # print out the value of the perimeter of the rectangle
    print(" The perimeter of the rectangle is " + str(P) + "cm")
    # draw a visual of the rectangle at smaller scale
    rect(25, 25, b, h)


perimeter_rect(60, 30)
