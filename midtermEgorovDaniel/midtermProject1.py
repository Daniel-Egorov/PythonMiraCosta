"""
{
    "File": "midtermProject1.py",
    "Author": "Daniel Egorov",
    "Date": "03/08/21",
    "Desc": [
        "A program to return statistics of a given file of numbers"
    ],
    "Algorithm": [
        "make a function for each math operation",
        "read the file given and split into a list by new lines",
        "rid of items in the list that cant be numbers",
        "inform user if list is empty (if no numbers are in file)",
        "sort the list for convenience",
        "use functions created to get stats"
    ]
}

"""

import math

def average(nums):
    return sum(nums) / len(nums)

def med(nums):
    if len(nums) % 2 == 0:
        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2 # return average of the two middle numbers, if list is even in length
    else:
        return nums[len(nums) // 2]

def standardDev(nums):
    avg = average(nums)
    variance = [(x - avg) ** 2 for x in nums]
    return math.sqrt(sum(variance) / len(variance))


def findStats(fileName):

    with open(fileName) as file:
        nums = file.read()

    nums = nums.split('\n') # convert file to list of numbers

    for i in range(len(nums)): # remove non numeric items from the list
        if not nums[i].isnumeric():
            del nums[i]
            continue
        try:
            nums[i] = float(nums[i])
        except:
            return 'Be sure each line has only one number'
            
    if len(nums) == 0: # the list will be empty if no numbers are in file
        return 'Be sure there are numbers in the file'
        

    nums.sort()

    mean = average(nums)
    median = med(nums)
    std = standardDev(nums)


    return f'Mean: {mean}\nMedian: {median}\nStandard Deviation: {std}'


def main():
    print(findStats('numbers.txt'))

main()
