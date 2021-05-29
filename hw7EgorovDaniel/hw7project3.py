"""
{
    "File": "hw7project3.py",
    "Author": "Daniel Egorov",
    "Date": "03/09/21",
    "Desc": [
        "A program to return the amount of a fine",
        "given the clocked speed as well as the speed limit"
    ],
    "Algorithm": [
        "gather inputs from user",
        "determine if speed is fine-able",
        "add 5 to the base fine for every 1mph over the speed limit",
        "add 200 to the new number if speed is over 90"
        "return the total fine"
    ]
}

"""


def speedingFine(speedLimit, clockedSpeed):
    if not speedLimit.isnumeric():
        return 'Speed limit inputted is not a number'

    if not clockedSpeed.isnumeric():
        return 'Clocked speed inputted is not a number'
    
    speedLimit = float(speedLimit)
    clockedSpeed = float(clockedSpeed)

    baseFine = 50

    if clockedSpeed <= speedLimit:
        return 'Clocked speed was legal'

    for i in range(int(clockedSpeed) - int(speedLimit)):
        baseFine += 5

    if clockedSpeed > 90:
        baseFine += 200

    return f'The fine is ${baseFine}'




def main():
    speedLimit = input('What is the speed limit?\n')
    clockedSpeed = input('What was the clocked speed?\n')
    print(speedingFine(speedLimit, clockedSpeed))


main()