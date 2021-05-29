"""
{
    "File": "hw9project2.py",
    "Author": "Daniel Egorov",
    "Date": "04/10/21",
    "Desc": [
        "a gui craps simulator that shows probability of winning"
    ],
    "Algorithm": [
        "initiate the two die as well as the buttons",
        "initiate variables to store wins losses roll count and initial roll",
        "allow user to roll the die, and store the total value of the die into the initial roll",
        "check each roll if the user had won/lost and if they have",
        "reset some variables to allow for the starting of a 'new' game",
        "allow the user to press the calculate button",
        "to see their current win/loss ratio",
        "end the program if they press the quit button"
    ]
}

"""
from graphics import *
from button import Button
from dieview import DieView
from random import randrange

def getValue(n):
    if n == 1 or n == 2 or n == 3 or n == 4 or n == 5:
        return n
    elif n == 6 or n == 7:
        return 6

def main():
    win = GraphWin('Craps simulator', 500, 500)

    die1 = DieView(win, Point(150, 150), 100)
    die2 = DieView(win, Point(350, 150), 100)

    rButton = Button(win, Point(250, 350), 50, 20, 'Roll')
    rButton.activate()

    cButton = Button(win, Point(250, 375), 120, 20, 'Calculate W/L')
    cText = Text(Point(250, 300), '').draw(win)

    qButton = Button(win, Point(250, 400), 50, 20, 'Quit')

    w = 0
    l = 0
    rollCount = 0

    initialRoll = None

    click = win.getMouse()
    while not qButton.clicked(click):
        if rButton.clicked(click):
            cText.setText('')

            cButton.deactivate() # disallow calculating before winning or losing
            qButton.activate()

            n1 = randrange(1, 7)
            die1.setValue(n1)

            n2 = randrange(1, 7)
            die2.setValue(n2)

            value1 = getValue(n1)
            value2 = getValue(n2)

            total = value1 + value2

            if initialRoll == None:
                initialRoll = total # set the initial roll if it hasnt been set yet

            if rollCount == 0:
                if total == 2 or total == 3 or total == 12:
                    cText.setText('Loss')

                    l += 1

                    cButton.activate()

                elif total == 7 or total == 11:
                    cText.setText('Win')

                    w += 1

                    cButton.activate()

                else:
                    rollCount += 1
                
            else:
                rollCount += 1

                if total == initialRoll:
                    cText.setText('Win')

                    w += 1
                    rollCount = 0
                    initialRoll = None # reset everything to initiate a new game

                    cButton.activate()

                elif total == 7:
                    cText.setText('Loss')

                    l += 1
                    rollCount = 0 
                    initialRoll = None # reset everything to initiate a new game

                    cButton.activate()

                
        elif cButton.clicked(click):
            prob = w / (w + l)
            cText.setText(f'Your probability of winning is {prob}')

            initialRoll = None 
            rollCount = 0 # reset everything to initiate a new game

        click = win.getMouse()


    # win.getMouse()

main()