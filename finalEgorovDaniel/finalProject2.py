"""
{
    "File": "finalProject2.py",
    "Author": "Daniel Egorov",
    "Date": "05/22/21",
    "Desc": [
        "a program to check the placement of a name",
        "in top 1000 boys and girls names"
    ],
    "Algorithm": [
        "read each file and create dictionary",
        "containing the name and the position of each name, with the name count",
        "ask for user input and check if their name is in the dictionaries",
        "if so, tell the user what position they are in the list, and how many",
        "are named with that name"
    ]
}

"""
def makeDict(filename):
    final = dict()
    with open(filename) as file:
        read = file.read()
        read = read.split('\n')

        for i in range(len(read)):
            temp = read[i]
            if temp == '':
                continue

            temp = temp.split(' ')

            final[temp[0].lower()] = [i + 1, temp[1]]


    return final




def main():
    boys = makeDict('boynames.txt')
    girls = makeDict('girlnames.txt')

    print('This program will check the ranking of boys and girls names')
    testName = input('What name would you like to check?\n')

    if testName.lower() in boys.keys():
        print(f'{testName} is ranked {boys[testName.lower()][0]} in popularity among boys with {boys[testName.lower()][1]} namings')
    else:
        print(f'{testName} is not ranked among the top 1000 boys names')

    if testName.lower() in girls.keys():
        print(f'{testName} is ranked {girls[testName.lower()][0]} in popularity among girls with {girls[testName.lower()][1]} namings')
    else:
        print(f'{testName} is not ranked among the top 1000 girls names')

main()