"""
{
    "File": "finalProject1.py",
    "Author": "Daniel Egorov",
    "Date": "05/22/21",
    "Desc": [
        "a program to spell check"
    ],
    "Algorithm": [
        "allow the user to input two files",
        "one to check for spelling",
        "and one to represent the dictionary",
        "binary search the dictionary for each word in the text file",
        "and if it's not in the dictionary, it's a potential misspell",
        "return a list to the user of potential misspells"
    ]
}

"""
from graphics import *
from button import Button

def binarySearch(array, search, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if array[mid] == search:
        return mid

    elif array[mid] > search:
        return binarySearch(array, search, low, mid -1)

    elif array[mid] < search:
        return binarySearch(array, search, mid + 1, high)

def spellCheck(dictionary, textFile):
    misspelled = []

    with open(dictionary) as file:
        dictionary = file.read().split('\n')

    for i in range(len(dictionary)):
        dictionary[i] = dictionary[i].lower() # make all words lowercase for ease

    with open(textFile) as file:
        read = file.read().split()

    for word in read:
        for letter in word:
            if not letter.isalpha():
                word = word.replace(letter, '')
        if binarySearch(dictionary, word.lower(), 0, len(dictionary) - 1) == -1:
            misspelled.append(word)
    return misspelled


def main():
    win = GraphWin('Spell Checker', 500, 500)
    title = Text(Point(250, 50), 'input a file to check, and then the dictionary to use').draw(win)

    textFileInput = Entry(Point(175, 100), 10).draw(win)
    dictFileInput = Entry(Point(325, 100), 10).draw(win)

    eButton = Button(win, Point(250, 150), 50, 20, 'Enter')
    eButton.activate()

    qButton = Button(win, Point(250, 450), 50, 20, 'Quit')

    text = Text(Point(250, 250), '').draw(win)

    click = win.getMouse()
    while not qButton.clicked(click):
        if eButton.clicked(click):
            text.setText('')

            textFile = textFileInput.getText()
            dictFile = dictFileInput.getText()

            misspelled = spellCheck(dictFile, textFile)
            if len(misspelled) > 0:
                text.setText('\n'.join(misspelled))
            else:
                text.setText('No misspelled words')

            qButton.activate()
        click = win.getMouse()

main()