# cbutton.py
from graphics import *
from math import sqrt

class CButton:

    def __init__(self, win, center, radius, label):

        self.x, self.y = center.getX(), center.getY()
        self.radius = radius

        self.circ = Circle(center, radius).draw(win)
        self.label = Text(center, label)
        self.label.draw(win)

        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        x1 = self.x
        x2 = p.getX()
        y1 = self.y
        y2 = p.getY()
        dX = x2 - x1
        dY = y2 - y1
        length = abs(sqrt((dX ** 2) + (dY ** 2)))

        return (self.active and
                length <= self.radius)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.circ.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.circ.setWidth(1)
        self.active = False