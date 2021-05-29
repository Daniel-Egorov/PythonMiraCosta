"""
{
    "File": "midtermProject2.py",
    "Author": "Daniel Egorov",
    "Date": "03/08/21",
    "Desc": [
        "A program that can encode, as well as decode caesar cipher"
    ],
    "Algorithm": [
        "Take the string and use a function",
        "to convert it to a list of numbers",
        "each number will represent a specific letter",
        "increment each number in the list by the shift value",
        "and if the value becomes greater than 25",
        "subtract 26 from it, to loop back into the alphabet",
        "rather than leaving it",
        "also add 26 to the value if its less than 0",
        "this handles negative shift values",
        "use a while loop for both steps above",
        "this handles shifts greater than 26",
        "and to decode the cipher, simply use the encode function",
        "but make the shift opposite of what was given",
        "to decode a cipher with a shift of 2",
        "simply encode with a shift of -2"
    ]
}

"""


def letterToNum(letter, customAlphabet = 'abcdefghijklmnopqrstuvwxyz'):
    letter = letter.lower()

    if not letter.isalpha(): # dont mess with non letter characters
        return letter

    customAlphabet = list(customAlphabet)

    return customAlphabet.index(letter)
    
    
def numsToLetter(num, customAlphabet = 'abcdefghijklmnopqrstuvwxyz'):
    if not type(num) == int: # dont mess with non letter characters
        return num

    customAlphabet = list(customAlphabet)

    return customAlphabet[num]



def encodeCaesar(string, shift, customAlphabet = 'abcdefghijklmnopqrstuvwxyz'):
    try:
        int(shift)
    except:
        return 'invalid shift value, must be integer.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in alphabet: # ensure custom alphabet is valid
        if not letter in customAlphabet:
            return f'Invalid alphabet, "{letter}" does not appear'
        if customAlphabet.count(letter) > 1:
            return f'Invalid alphabet, "{letter}" is repeatead'

    numsList = []

    for i in range(len(string)): # convert letters to nums, add to list
        numsList.append(letterToNum(string[i], customAlphabet))

    for i in range(len(numsList)): # handle the shifting
        if not type(numsList[i]) == int:
            continue

        numsList[i] += shift
        while numsList[i] > 25: 
            numsList[i] -= 26
#                               while loops to handle shifts that extend beyond 0-26
        while numsList[i] < 0:
            numsList[i] += 26

    lettersList = []

    for i in range(len(numsList)): # convert the new numbers back to letters
        if string[i] == string[i].upper():
            lettersList.append(numsToLetter(numsList[i], customAlphabet).upper()) # maintain uppercase letters
        else:
            lettersList.append(numsToLetter(numsList[i], customAlphabet))

    return ''.join(lettersList) # form the final string

def decodeCaesar(string, shift, customAlphabet = 'abcdefghijklmnopqrstuvwxyz'):
    return encodeCaesar(string, -shift, customAlphabet) # encode with opposite shift, to decode

def main():
    # customAlphabet = 'pyfgcrlaoeuidhtnsqjkxbmwvz'

    print(encodeCaesar('this message will be encoded', 7))

    print(decodeCaesar('guvf zrffntr unf orra qrpbqrq', 13))


main()