from math import sin, pi
def main():
    height = float(input('How many units is the height of the wall where your ladder reaches? '))
    angle = float(input('What is the angle of the ladder? (in degrees) '))
    radians = angle * (pi / 180)
    length = round(height/sin(radians), 3)
    print(f'Your ladder is {length} units long')
main()