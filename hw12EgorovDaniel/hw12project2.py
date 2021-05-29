"""
{
    "File": "hw12project2.py",
    "Author": "Daniel Egorov",
    "Date": "05/01/21",
    "Desc": [
        "a program to check if a word or phrase is a palindrome"
    ],
    "Algorithm": [
        "recursively check if the first and last character",
        "of a string are the same, and then remove them if they are",
        "otherwise it's not a palindrome",
    ]
}

"""

def isPalindrome(s):
    for char in s:
        if not char.isalpha():
            s = s.replace(char, '')

    s = s.lower()

    if len(s) == 1 or len(s) == 0:
        return True

    if s[0] == s[-1]:
        s = s[1:-1]

    elif s[0] != s[-1]:
        return False

    return isPalindrome(s)


def main():
    print('This program will check if a word or phrase is a palindrome\n')

    phrase = input('What phrase would you like to test?\n')

    check = isPalindrome(phrase)

    if check == True:
        print('Your phrase is a palindrome')

    elif check == False:
        print('Your phrase is not a palindrome')

main()