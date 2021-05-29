from math import pi
def main():
    # cost of pizza
    cost = float(input('What is the cost of the pizza? (in $) '))
    # diameter of pizza
    diameter = float(input('What is the diameter of the pizza? (in Inches) '))
    # find radius for the math
    radius = diameter/2
    # area in inches squared, of the pizza
    area = pi * (radius ** 2)
    # cost per square inch, in dollars
    answer = round(cost/area, 2)
    print(f'${answer}')
main()