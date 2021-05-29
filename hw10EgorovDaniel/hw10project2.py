"""
{
    "File": "hw10project2.py",
    "Author": "Daniel Egorov",
    "Date": "04/17/21",
    "Desc": [
        "a program to display a given suit of cards"
    ],
    "Algorithm": [
        "initiate the window and all buttons and entry window",
        "sit in a while loop while the user hasnt clicked the quit button",
        "when the user presses the enter button, get the text from the entry window",
        "and display the suit icon based on the suit typed into the entry window"
    ]
}

"""
from graphics import *
from button import Button


def main():
    win = GraphWin('Card Suit Displayer', 500, 500)

    text = Text(Point(250, 50), 'Type the name of the suit you would like to see').draw(win)

    inputWin = Entry(Point(250, 75), 10).draw(win)

    eButton = Button(win, Point(250, 100), 50, 25, 'Enter')
    eButton.activate()

    qButton = Button(win, Point(250, 450), 50, 25, 'Quit')
    qButton.activate()

    image = Image(Point(250, 250), 'S.png').draw(win)

    click = win.getMouse()
    while not qButton.clicked(click):
        if eButton.clicked(click):
            suit = inputWin.getText().lower()


            if suit == 'spades':
                image.undraw()
                image = Image(Point(250, 250), 'S.png').draw(win)

            elif suit == 'clubs':
                image.undraw()
                image = Image(Point(250, 250), 'C.png').draw(win)

            elif suit == 'diamonds':
                image.undraw()
                image = Image(Point(250, 250), 'D.png').draw(win)

            elif suit == 'hearts':
                image.undraw()
                image = Image(Point(250, 250), 'H.png').draw(win)

        click = win.getMouse()

    
main()