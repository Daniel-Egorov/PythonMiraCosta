"""
{
    "File": "midtermProject3.py",
    "Author": "Daniel Egorov",
    "Date": "03/11/21",
    "Desc": [
        "A program that allows you to draw dot to dot pictures"
    ],
    "Algorithm": [
        "Initiate a for loop that allows the user to click up to 100 times",
        "create a 'button' that will allow the user to quit placing dots",
        "if they don't want to place 100",
        "add each dot they do to a list for later use",
        "after all dots have been placed, access previous list to draw the lines",
        "also add numbers to the canvas 10 pixels off the dot to label them",
        "append said numbers to another list for easy removal in the future",
    ]
}

"""

from graphics import *




def main():
    win = GraphWin('Create connect the dot picture!', 1000, 1000)

    title = Text(Point(500, 50), '').draw(win)
    title.setText('Click up to 100 times to make a dot-to-dot image')
    quitButton = Rectangle(Point(375, 925), Point(625, 975)).draw(win)
    quitButton.setFill('gray')

    quitText = Text(Point(500, 950), '').draw(win)
    quitText.setText('Click here to finish drawing early')

    points = []
    count = 0
    pointNums = []

    for i in range(100):
        click = win.getMouse()
        if click.getX() >= 375 and click.getX() <= 625 and click.getY() >= 925 and click.getY() <= 975:
            quitText.undraw()
            quitButton.undraw()
            break
        else:
            points.append(click)
            count += 1

            Point(click.getX(), click.getY()).draw(win)

            text = Text(Point(click.getX() - 10, click.getY() - 10), str(count)).draw(win)
            pointNums.append(text)

    for i in range(len(points)):
        if i == 0:
            continue
        else:
            Line(points[i-1], points[i]).draw(win)



    title.setText('Here is your dot-to-dot! Click anywhere to remove the numbers')
    win.getMouse()
    
    for i in range(len(pointNums)):
        pointNums[i].undraw()


    title.setText('Here is your dot-to-dot! Click anywhere to quit!')
    win.getMouse()

main()