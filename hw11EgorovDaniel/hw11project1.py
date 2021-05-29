"""
{
    "File": "hw11project1.py",
    "Author": "Daniel Egorov",
    "Date": "04/24/21",
    "Desc": [
        "a modified program to play dice poker"
    ],
    "Algorithm": [
        "take the original dice poker program",
        "add a screen by drawing a new 'background'",
        "relay information on top of that screen and allow buttons",
        "to be pressed to show or hide the information",
        "once the user decides they want to play",
        "undraw all the information and 'background'",
        "to reveal the actual game screen",
        "finally, run the game"
    ]
}

"""

from graphics import *
from pokerapp import PokerApp
from button import Button
from cdieview import ColorDieView

class HelpScreen:
    def __init__(self, win):
        self.win = win

        self.help1 = Text(Point(300, 150), 'Rolls Cost $10 per')
        self.help2 = Text(Point(300, 170), 'Rolling 5 of a kind returns $30')
        self.help3 = Text(Point(300, 190), 'Rolling 4 of a kind returns $15')
        self.help4 = Text(Point(300, 210), 'Rolling 3 of a kind and 2 of a kind returns $12')
        self.help5 = Text(Point(300, 230), 'Rolling 3 of a kind returns $8')
        self.help6 = Text(Point(300, 250), 'Rolling either a 1-5 or a 2-6 returns $20')
        self.help7 = Text(Point(300, 270), 'Rolling two pairs returns $5')
        self.help8 = Text(Point(300, 290), 'Otherwise, you get nothing :)')

        self.shown = False

    def show(self):
        if self.shown == False:
            self.help1.draw(self.win)
            self.help2.draw(self.win)
            self.help3.draw(self.win)
            self.help4.draw(self.win)
            self.help5.draw(self.win)
            self.help6.draw(self.win)
            self.help7.draw(self.win)
            self.help8.draw(self.win)

            self.shown = True



    def hide(self):
        if self.shown == True:
            self.help1.undraw()
            self.help2.undraw()
            self.help3.undraw()
            self.help4.undraw()
            self.help5.undraw()
            self.help6.undraw()
            self.help7.undraw()
            self.help8.undraw()

            self.shown = False



class GraphicsInterface:

    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300,30), "Python  Poker  Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300,380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300,100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300,170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570,375), 40, 30, "Quit")
        self.buttons.append(b)
        self.money = Text(Point(300,325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    def createDice(self, center, size):
        center.move(-3*size,0)
        self.dice = []
        for i in range(5):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size,0)

    def addDiceButtons(self, center, width, height):
        center.move(-3*width, 0)
        for i in range(1,6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)

    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def showResult(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"

    def close(self):
        self.win.close()

    def chooseDice(self):
        # choices is a list of the indexes of the selected dice
        choices = []                   # No dice chosen yet
        while True: 
            # wait for user to click a valid button
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
                             "Roll Dice", "Score"])

            if b[0] == "D":            # User clicked a die button
                i = eval(b[4]) - 1     # Translate label to die index
                if i in choices:       # Currently selected, unselect it
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:                  # Currently unselected, select it
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:                      # User clicked Roll or Score
                for d in self.dice:    # Revert appearance of all dice
                    d.setColor("black")
                if b == "Score":       # Score clicked, ignore choices
                    return []
                elif choices != []:    # Don't accept Roll unless some
                    return choices     #   dice are actually selected

    
    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()  # function exit here.


def main():
    inter = GraphicsInterface()

    fore = Rectangle(Point(0, 0), Point(600, 400)).draw(inter.win)
    fore.setFill('green3')

    title = Text(Point(300, 50), 'Welcome to Dice Poker').draw(inter.win)
    info = Text(Point(300, 100), 'This program will allow you to play Dice Poker\nand bet fake money whilst doing so\nclick any of the buttons below').draw(inter.win)

    qButton = Button(inter.win, Point(550, 350), 40, 20, 'Exit')
    qButton.activate()

    pButton = Button(inter.win, Point(300, 350), 40, 20, 'Play')
    pButton.activate()

    hButton = Button(inter.win, Point(50, 350), 40, 20, 'Help')
    hButton.activate()

    hScreen = HelpScreen(inter.win)

    while True:
        click = inter.win.getMouse()

        if qButton.clicked(click):
            inter.close()
            return

        elif pButton.clicked(click):
            fore.undraw()
            qButton.remove()
            pButton.remove()
            hButton.remove()
            title.undraw()
            info.undraw()
            hScreen.hide()
            break

        elif hButton.clicked(click):
            if hScreen.shown == True:
                hScreen.hide()

            elif hScreen.shown == False:
                hScreen.show()

    app = PokerApp(inter)
    app.run()

if __name__ == '__main__':
    main()