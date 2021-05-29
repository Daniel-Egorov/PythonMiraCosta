"""
{
    "File": "hw10project1.py",
    "Author": "Daniel Egorov",
    "Date": "04/17/21",
    "Desc": [
        "a program to count the number of keywords used in a python file"
    ],
    "Algorithm": [
        "have a list of all keywords to check",
        "ask user for the name of the file they want to check",
        "open the file and read it, and separate it into a list of each word",
        "iterate through said list and append each word to a new list, if it is a keyword",
        "iterate through the set keyword list to get a new list with a count of each keyword",
        "^^^ if greater than 0 ^^^",
        "then iterate through the list of counts and print to the user the amount of keywords"
    ]
}

"""


def main():

    keywords = [
        'False', 
        'None', 
        'True', 
        'and', 
        'as', 
        'assert', 
        'break', 
        'class', 
        'continue', 
        'def', 
        'del', 
        'elif', 
        'else', 
        'except', 
        'finally', 
        'for', 
        'from', 
        'global', 
        'if', 
        'import', 
        'in', 
        'is', 
        'lambda', 
        'nonlocal', 
        'not', 
        'or', 
        'pass', 
        'raise', 
        'return', 
        'try', 
        'while', 
        'with', 
        'yield'
    ]

    print('This program will count how many keywords are in a python file for you\n')

    fileName = input('What is the name of your python file? (no .py)\n')

    with open(f'{fileName}.py') as file:
        read = file.read()
        words = read.split()

    foundWords = []

    for i in range(len(words)):
        if words[i] in keywords:
            foundWords.append(words[i])

    wordCounts = []

    for i in range(len(keywords)):
        if words.count(keywords[i]) != 0:
            wordCounts.append((keywords[i], words.count(keywords[i])))

    wordCounts.append(('total', len(foundWords)))

    for i in range(len(wordCounts)):
        print(f'{wordCounts[i][0]}: {wordCounts[i][1]}')


main()