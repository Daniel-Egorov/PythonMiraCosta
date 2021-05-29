"""
{
    "File": "hw7project2.py",
    "Author": "Daniel Egorov",
    "Date": "03/09/21",
    "Desc": [
        "A program to predict adult child height",
        "given the mother and fathers height"
    ],
    "Algorithm": [
        "function that takes the heights and gender as parameters",
        "feed the heights into the equation",
        "return the height in feet, with remainder of inches"
    ]
}

"""

def heightReturn(fatherHeight, motherHeight, childGender):
    if not fatherHeight.isnumeric():
        return 'Fathers height isnt a number'
    if not motherHeight.isnumeric():
        return 'Mothers height isnt a number'

    fatherHeight = float(fatherHeight)
    motherHeight = float(motherHeight)

    if childGender.lower() == 'male':
        height = ((motherHeight * (13/12)) + fatherHeight) / 2

    elif childGender.lower() == 'female':
        height = ((fatherHeight * (12/13)) + motherHeight) / 2

    else:
        return 'Input either male or female for the gender'

    return f'{height // 12} feet {round(height % 12, 2)} inches'



def main():
    fatherHeight = input('What is the height of the father?\n')
    motherHeight = input('What is the height of the mother?\n')
    childGender = input('What is the gender of the child?\n')

    print(heightReturn(fatherHeight, motherHeight, childGender))



main()