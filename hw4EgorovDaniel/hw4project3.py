import graphics as gp
from math import sqrt
def main():
    window = gp.GraphWin('Draw a line!', 500, 500)

    title = gp.Text(gp.Point(250, 20), 'Click on the screen in two locations to form a line!')
    title.draw(window)

    slopeText = gp.Text(gp.Point(250, 450), '')
    slopeText.draw(window)

    lengthText = gp.Text(gp.Point(250, 425), '')
    lengthText.draw(window)

    midpointText = gp.Text(gp.Point(250, 475), '')
    midpointText.draw(window)

    point1 = window.getMouse()
    point2 = window.getMouse()

    line = gp.Line(point1, point2)
    line.draw(window)

    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    dX = x2 - x1
    dY = y2 - y1

    point3 = gp.Point(x1 + (dX / 2), y1 + (dY / 2))
    point3.draw(window)
    point3.setFill('cyan')

    slope = dY / dX
    length = sqrt((dX ** 2) + (dY ** 2))

    slopeText.setText(f'Slope: {round(slope, 3)}')
    lengthText.setText(f'Length: {round(length, 3)}')
    midpointText.setText(f'Midpoint (in cyan): ({round(point3.getX(), 1)}, {round(point3.getY(), 1)})')

    title.setText('Click anywhere to quit')
    window.getMouse()
main()