"""
{
    "File": "hw7project1.py",
    "Author": "Daniel Egorov",
    "Date": "03/09/21",
    "Desc": [
        "A program to return the letter grade",
        "given the percetage of points earned"
    ],
    "Algorithm": [
        "A function that uses if and elif statements",
        "to determine what the letter grade is"
    ]
}

"""

def returnGrade(percent):

    try:
        percent = float(percent)
    except:
        return 'Make sure you input a number'

    if percent >= 90 and percent <= 100:
        return 'Your letter grade is: A'

    elif percent >= 80 and percent <= 89.99:
        return 'Your letter grade is: B'

    elif percent >= 70 and percent <= 79.99:
        return 'Your letter grade is: C'

    elif percent >= 60 and percent <= 69.99:
        return 'Your letter grade is: D'

    elif percent >= 0 and percent <= 59.99:
        return 'Your letter grade is: F'





def main():
    percent = input('What is your percetage of earned points in the class?\n')

    print(returnGrade(percent))

main()