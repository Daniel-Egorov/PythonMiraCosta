import graphics as gp

def main():
    win = gp.GraphWin('Draw a house!', 500, 500)

    title = gp.Text(gp.Point(250, 20), 'Click two opposing corners for your house frame')
    title.draw(win)

    corner1 = win.getMouse()
    corner2 = win.getMouse()

    if corner1.getY() < corner2.getY():
        frameLowPoint = corner2
        frameHighPoint = corner1
    elif corner1.getY() > corner2.getY():
        frameLowPoint = corner1
        frameHighPoint = corner2

    frame = gp.Rectangle(corner1, corner2)
    frame.draw(win)

    title.setText('Click where you want the top of the door')

    topOfDoor = win.getMouse()
    doorWidth = abs(corner2.getX() - corner1.getX()) / 5
    topLeftDoor = gp.Point(topOfDoor.getX() - (doorWidth / 2), topOfDoor.getY())
    bottomRightDoor = gp.Point(topOfDoor.getX() + (doorWidth / 2), frameLowPoint.getY())
    door = gp.Rectangle(topLeftDoor, bottomRightDoor)
    door.draw(win)

    title.setText('Click where you want the center of the window')

    windowWidth = (bottomRightDoor.getX() - topLeftDoor.getX()) / 2
    windowCenter = win.getMouse()
    windowTopLeft = gp.Point(windowCenter.getX() - (windowWidth / 2), (windowCenter.getY() - (windowWidth / 2)))
    windowBotRight = gp.Point(windowCenter.getX() + (windowWidth / 2), (windowCenter.getY() + (windowWidth / 2)))
    window = gp.Rectangle(windowTopLeft, windowBotRight)
    window.draw(win)

    title.setText('Click where you want the peak of the roof')

    roofP3 = win.getMouse()
    roofP1 = gp.Point(corner1.getX(), frameHighPoint.getY())
    roofP2 = gp.Point(corner2.getX(), frameHighPoint.getY())
    roof = gp.Polygon(roofP1, roofP2, roofP3)
    roof.draw(win)

    title.setText('Click anywhere to quit')
    win.getMouse()
main()