"""
{
    "File": "hw6project1.py",
    "Author": "Daniel Egorov",
    "Date": "03/03/21",
    "Desc": [
        "A program that has two functions",
        "One to return the area of a sphere",
        "And another to return the volume of a sphere",
        "Each given the radius of the sphere"
    ],
    "Algorithm": [
        "To calculate the surface area of a sphere",
        "You do 4(pi)(radius^2)",
        "To calculate the volume of a sphere",
        "You do (4/3)(pi)(radius^3)"
    ]
}

"""
from math import pi

def sphereArea(radius):
    return round(4 * pi * (radius ** 2), 4)

def sphereVolume(radius):
    return round((4/3) * pi * (radius ** 3), 4)

def main():
    radius1 = 12
    radius2 = 43
    print(f'The surface area of sphere 1 is {sphereArea(radius1)} units squared')
    print(f'The volume of sphere 1 is {sphereVolume(radius1)} units cubed')
    print(f'The surface area of sphere 2 is {sphereArea(radius2)} units squared')
    print(f'The volume of sphere 2 is {sphereVolume(radius2)} units cubed')

main()