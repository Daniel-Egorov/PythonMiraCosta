"""
{
    "File": "hw10extraCredit.py",
    "Author": "Daniel Egorov",
    "Date": "04/17/21",
    "Desc": [
        "a program to display any card that the user wants"
    ],
    "Algorithm": [
        "initiate the window with all the entry windows and buttons",
        "enter while loop that loops until user clicks quit",
        "once user presses enter, grab the text from each box",
        "and change the information on the card to match the users specifications"
    ]
}

"""
from graphics import *
from button import Button


def main():
    win = GraphWin('Card Suit Displayer', 500, 500)

    text = Text(Point(250, 50), 'Type the name of the suit you would like to see').draw(win)

    valWin = Entry(Point(300, 75), 10).draw(win)
    suitWin = Entry(Point(200, 75), 10).draw(win)
    valText = Text(Point(300, 100), 'Value').draw(win)
    suitText = Text(Point(200, 100), 'Suit').draw(win)

    eButton = Button(win, Point(250, 415), 50, 25, 'Enter')
    eButton.activate()

    qButton = Button(win, Point(250, 450), 50, 25, 'Quit')
    qButton.activate()

    image = Image(Point(250, 250), 'S.png').draw(win)
    cardRect = Rectangle(Point(150, 125), Point(350, 375)).draw(win)
    cardValue = Text(Point(175, 150), 'A').draw(win)

    click = win.getMouse()
    while not qButton.clicked(click):
        if eButton.clicked(click):

            suit = suitWin.getText().lower()
            value = valWin.getText().lower()

            if value != 'ace' and value != 'king' and value != 'queen' and value != 'jack':
                cardValue.setText(value)
            
            elif value == 'ace' or value == 'king' or value == 'queen' or value == 'jack':
                cardValue.setText(value[0].upper())

            if suit == 'diamonds' or suit == 'hearts':
                cardValue.setTextColor('red')

            elif suit == 'spades' or suit == 'clubs':
                cardValue.setTextColor('black')

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