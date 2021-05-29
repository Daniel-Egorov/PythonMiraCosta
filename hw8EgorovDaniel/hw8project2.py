"""
{
    "File": "hw8project2.py",
    "Author": "Daniel Egorov",
    "Date": "04/02/21",
    "Desc": [
        "a program to convert an image to grayscale",
        "and save the resulting image"
    ],
    "Algorithm": [
        "initialize graphwin with a text box for input",
        "wait for the user to input a filename",
        "display the image specified on the canvas",
        "wait for user to press button to convert to mono",
        "create a duplicate of the image that will get modified",
        "convert the image to mono by iterating through each pixel",
        "by using nested for loops",
        "use weighted average to find the brightness of the gray",
        "edit each pixel of the duplicate to the respective brightness of gray",
        "display the new image and prompt user to input filename",
        "save said image under said filename"
    ]
}

"""
from graphics import *

def inButton(click):
    if click.getX() >= 450 and click.getX() <= 550 and click.getY() >= 150 and click.getY() <= 200:
        return True
    return False # function to check if user clicked inside button bounding box

def main():
    win = GraphWin('Convert Image to Grayscale', 1000, 1000)

    text = Text(Point(500, 50), 'What is the file you want to convert? (including extension)').draw(win)

    inputWin = Entry(Point(500, 100), 10).draw(win)

    button = Rectangle(Point(450, 150), Point(550, 200)).draw(win)
    buttonText = Text(Point( 500, 175), 'Enter').draw(win) # create a button to submit an image

    click = win.getMouse()
    while not inButton(click): # force user to click the button :)
        click = win.getMouse()

    imageFile = inputWin.getText()

    image = Image(Point(500, 500), imageFile).draw(win)

    imageMono = Image(Point(500, 500), imageFile)

    for i in range(imageMono.getHeight()):
        for j in range(imageMono.getWidth()):
            pixel = image.getPixel(j, i)
            brightness = int(round((0.299 * pixel[0]) + (0.587 * pixel[1]) + (0.114 * pixel[2])))
            imageMono.setPixel(j, i, color_rgb(brightness, brightness, brightness))

    text.setText('Click the button to see the monochrome image')

    click = win.getMouse()
    while not inButton(click):
        click = win.getMouse()

    imageMono.draw(win)
    image.undraw() # display mono image and remove chrome image

    inputWin.undraw()
    inputWin = Entry(Point(500, 100), 10).draw(win) # reset the input window

    text.setText('Type the name you want the new image to save under (including extension)')

    click = win.getMouse()
    while not inButton(click):
        click = win.getMouse()

    saveFile = inputWin.getText()
    imageMono.save(saveFile)

    text.setText('Click anywhere to quit')

    win.getMouse()

main()