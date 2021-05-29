"""
{
    "File": "hw6project2.py",
    "Author": "Daniel Egorov",
    "Date": "03/03/21",
    "Desc": [
        "A program to return the sum of a list of numbers",
        "using a function of course"
    ],
    "Algorithm": [
        "take list of numbers and use sum(), return the result",
        "use rng to generate the numbers used for testing"
    ]
}

"""
import random

# simply use the sum() function
def sumList(nums):
    return sum(nums)
    """
    also possible:
    
    total = 0
    for num in nums:
        total += num
    return total

    """

# use random module to generate the test numbers
def genList(numAmount, minimum, maximum):
    nums = []
    for i in range(numAmount):
        nums.append(random.randint(minimum, maximum))
    return nums

# execute the sumList() function with the generated numbers
def main():
    for i in range(3):
        nums = genList(15, 0, 100)
        print(f'Generated: {nums}')
        print(f'Summed: {sumList(nums)}')

main()