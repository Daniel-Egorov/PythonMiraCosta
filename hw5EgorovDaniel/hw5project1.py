

def makeAcronym(phrase):
    acronym = ''

    phrase = phrase.split()

    for word in phrase:
        acronym += word[0].upper()

    return f'Your acronym is {acronym}'

userInput = input('What phrase do you want to make an acronym?\n')

print(makeAcronym(userInput))