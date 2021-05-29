"""
{
    "File": "hw11project2.py",
    "Author": "Daniel Egorov",
    "Date": "04/24/21",
    "Desc": [
        "a program to allow someone to log into their bank account"
    ],
    "Algorithm": [
        "use a json file to store the data because i love json files so much they are the greatest method of storing data ever and i user them all the time because they are just so great",
        "ask the user for a ID and a PIN",
        "use a function to check if the credentials are valid",
        "if they are, Great Job!!!",
        "otherwise, let the user try again because they seem to be having a rough time :("
    ]
}

"""
import json

def authorized(userID, pin, data):
    if not userID in data.keys():
        return False
    if not data[userID]['pin'] == pin:
        return False
    return True

def main():

    with open('bankinfo.json') as file:
        data = json.load(file)

    while True:
        userID = input('What is your user ID?\n')
        pin = input('What is your PIN?\n')
        
        if authorized(userID, pin, data):
            print('Authorized')
            break

        elif not authorized(userID, pin, data):
            print('Invalid Credentials')


main()