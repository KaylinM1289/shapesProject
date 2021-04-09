# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
from math import pi


def calculateAreaOfCircle():
    r = float(input("input the radius of the circle: "))
    area = math.pi * r * r
    print(f'The area of the circle is {area}')
    print(area)


def calculatePerimeterOfCircle():
    r = float(input("input the radius of the circle: "))
    perimeter = 2 * math.pi * r
    print(f'The perimeter of the circle is {perimeter}')
    print(perimeter)


# Use a breakpoint in the code line below to debug your script.
# print(f'The area, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculatePerimeterOfCircle()
