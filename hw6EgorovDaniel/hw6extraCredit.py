"""
{
    "File": "hw6extraCredit.py",
    "Author": "Daniel Egorov",
    "Date": "03/03/21",
    "Desc": [
        "A program that will draw a new circle",
        "centered around where the user clicks",
        "for a total of ten times"
    ],
    "Algorithm": [
        "Initialize the program by drawing a circle in the center",
        "let user know they can move the circle 10 more times",
        "change the circle's position by undrawing the previous circle",
        "and redrawing the circle where the user clicked",
        "save the new circle into a variable so later it can be seen as the previous circle"
    ]
}

"""

from graphics import *

# draw the first circle that appears
def initCircle(win):
    circle = Circle(Point(250, 250), 50)
    circle.draw(win)
    return circle

# undraw and redraw the circle where the center is described
def moveTo(win, circle, center):
    circle.undraw()
    circle = Circle(center, 50)
    circle.draw(win)
    return circle

# execute the program
def main():
    win = GraphWin("Draw Some Circles!", 500, 500)
    title = Text(Point(250, 50), '').draw(win)
    circle = initCircle(win)
    for i in range(10):
        title.setText(f'Click anywhere to move the circle\'s center! ({10-i} more times)')
        circle = moveTo(win, circle, win.getMouse())
    title.setText('Click anywhere to quit')
    win.getMouse()


main()