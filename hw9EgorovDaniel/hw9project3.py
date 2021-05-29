"""
{
    "File": "hw9project3.py",
    "Author": "Daniel Egorov",
    "Date": "04/10/21",
    "Desc": [
        "A GUI version of hw7project2",
        "a program to estimate the height of a child as an adult",
        "given the heights of the parents, as well as the child's gender",
        "--- a slightly modified version of hw9project1.py ---"
    ],
    "Algorithm": [
        "create GraphWin with entry boxes for all parameters",
        "create a submit button so we know the user has typed their parameters",
        "create a quit button so the user can end the program at any time",
        "do the math given based on the gender and return the answer to the user",
        "make the buttons CButton rather than normal buttons"
    ]
}

"""

from graphics import *
from cbutton import CButton


def heightReturn(fatherHeight, motherHeight, childGender):

    try:
        fatherHeight = float(fatherHeight)
        motherHeight = float(motherHeight)
    except:
        return 'Ensure both heights are numbers'

    if childGender.lower() == 'male':
        height = ((motherHeight * (13/12)) + fatherHeight) / 2

    elif childGender.lower() == 'female':
        height = ((fatherHeight * (12/13)) + motherHeight) / 2

    else:
        return 'Input either "male" or "female" for the gender'

    return f'{height // 12} feet {round(height % 12, 2)} inches'



def main():
    win = GraphWin('Calculate a child\'s height', 500, 500)

    qButton = CButton(win, Point(250, 450), 20, 'Quit')
    qButton.activate()

    title = Text(Point(250, 50), 'Enter height values and press submit').draw(win)

    mHeightText = Text(Point(100, 125), 'Mother\'s height').draw(win)
    mHeightBox = Entry(Point(100, 150), 10).draw(win)

    fHeightText = Text(Point(250, 125), 'Father\'s height').draw(win)
    fHeightBox = Entry(Point(250, 150), 10).draw(win)

    cGenderText = Text(Point(400, 125), 'Child\'s gender').draw(win)
    cGenderBox = Entry(Point(400, 150), 10).draw(win)

    sButton = CButton(win, Point(250, 300), 30, 'Submit')
    sButton.activate()

    answerText = Text(Point(250, 200), '').draw(win)

    click = win.getMouse()
    while not qButton.clicked(click):
        if sButton.clicked(click):
            mHeight = mHeightBox.getText()

            fHeight = fHeightBox.getText()

            cGender = cGenderBox.getText()

            answerText.setText(heightReturn(fHeight, mHeight, cGender))

        click = win.getMouse()


    win.close()

main()