"""
{
    "File": "hw11project2.py",
    "Author": "Daniel Egorov",
    "Date": "04/24/21",
    "Desc": [
        .
    ],
    "Algorithm": [
        .
    ]
}

"""
import json
from graphics import *
from button import Button

class LoginScreen:
    def __init__(self, win):
        self.win = win

        self.title = Text(Point(300, 50), 'Welcome to Bank of Daniel')

        self.userIDtext = Text(Point(250, 100), 'User ID:')
        self.userIDentry = Entry(Point(330, 100), 10)

        self.pinText = Text(Point(250, 125), 'PIN:')
        self.pinEntry = Entry(Point(330, 125), 10)

        self.lButton = Button(win, Point(300, 175), 50, 20, 'Login')
        self.lButton.remove()

        self.qButton = Button(win, Point(300, 200), 50, 20, 'Quit')
        self.qButton.remove()

        self.shown = False

    def show(self):
        if self.shown == False:
            self.title.draw(self.win)
            self.userIDtext.draw(self.win)
            self.userIDentry.draw(self.win)
            self.pinText.draw(self.win)
            self.pinEntry.draw(self.win)
            self.lButton.unremove()
            self.lButton.activate()
            self.qButton.unremove()
            self.qButton.activate()
            self.shown = True

    def hide(self):
        if self.shown == True:
            self.title.undraw()
            self.userIDtext.undraw()
            self.userIDentry.undraw()
            self.pinText.undraw()
            self.pinEntry.undraw()
            self.lButton.remove()
            self.qButton.remove()
            self.shown = False


class HomeScreen:
    def __init__(self, win, userID):
        self.win = win
        self.userID = userID

        with open('bankinfo.json') as file:
            self.data = json.load(file)

        self.title = Text(Point(300, 50), 'Your account info')
        self.title.setSize(24)
        
        cBal = self.data[self.userID]['checking']
        sBal = self.data[self.userID]['savings']

        self.cBalText = Text(Point(225, 150), f'Checking:\n${cBal}')
        self.cBalText.setSize(18)
        self.sBalText = Text(Point(375, 150), f'Savings:\n${sBal}')
        self.sBalText.setSize(18)

        self.wButton = Button(self.win, Point(300, 200), 80, 20, 'Withdraw')
        self.wButton.remove()
        self.tButton = Button(self.win, Point(300, 225), 80, 20, 'Transfer')
        self.tButton.remove()

        self.shown = False

    def show(self):
        if self.shown == False:
            self.title.draw(self.win)
            self.cBalText.draw(self.win)
            self.sBalText.draw(self.win)
            self.wButton.unremove()
            self.wButton.activate()
            self.tButton.unremove()
            self.tButton.activate()
            self.shown = True


def main():
    with open('bankinfo.json') as file:
        data = json.load(file)

    win = GraphWin('ATM', 600, 600)

    lScreen = LoginScreen(win)
    lScreen.show()

    while True:
        click = win.getMouse()


    win.getMouse()

main()