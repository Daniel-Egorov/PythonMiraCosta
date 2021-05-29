import graphics as gp

window = gp.GraphWin('Shapes', 400, 400)

circle = gp.Circle(gp.Point(100, 100), 25)
circle.draw(window)

square = gp.Rectangle(gp.Point(150, 150), gp.Point(175, 175))
square.draw(window)

triangle = gp.Polygon(gp.Point(200, 200), gp.Point(300, 150), gp.Point(150, 275))
triangle.draw(window)

window.getMouse()