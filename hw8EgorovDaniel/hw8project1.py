"""
{
    "File": "hw8project1.py",
    "Author": "Daniel Egorov",
    "Date": "04/02/21",
    "Desc": [
        "A program that calculates the Nth Fibonacci number"
    ],
    "Algorithm": [
        "function that returns 1 if the user",
        "wants the first or second fibonacci number",
        "otherwise the function will loop N - 2 times",
        "appending the next fibonacci number to the list each time",
        "at the end, return the last number in the list",
        "it will be the one the user requested"
    ]
}

"""

def fib(num):
    if num < 1:
        return 'Input a positive integer' # self explanatory

    if num == 1 or num == 2:
        return 1 # return 1 if the user requests either of the first two numbers in sequence

    fibs = [1, 1] # initialize the fibonacci numbers list

    for i in range(num - 2):
        fibs.append(fibs[-1] + fibs[-2]) # add the next fibonacci number to the list

    return fibs[-1]




def main():
    num = input('What Nth Fibonacci number would you like?\n')
    
    try:
        num = int(num)

    except Exception:
        print('Input an integer')
        return

    print(fib(num))

main()