"""
{
    "File": "hw13project1.py",
    "Author": "Daniel Egorov",
    "Date": "05/06/21",
    "Desc": [
        "program to test different sorting methods"
    ],
    "Algorithm": [
        "functions to do sorting",
        "function to test all the methods",
        "test all methods and log results"
    ]
}

"""
import time

def selectionSort(nums):
    n = len(nums)

    for bottom in range(n - 1):
        mp = bottom
        for i in range(bottom + 1, n):
            if nums[i] < nums[mp]:
                mp = i

        nums[bottom], nums[mp] = nums[mp], nums[bottom]

    return nums

def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums)//2

        L = nums[:mid]
        R = nums[mid:]

        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1
    return nums

def pythonSort(nums):
    nums.sort()
    return nums

def test(filename):
    with open(filename) as file:
        read = file.read()

    nums = [int(x) for x in read.split('\n') if not x == '']

    start = time.perf_counter()
    pythonSort(nums)
    end = time.perf_counter()

    pythonTime = end - start

    start = time.perf_counter()
    selectionSort(nums)
    end = time.perf_counter()

    selectionTime = end - start

    start = time.perf_counter()
    mergeSort(nums)
    end = time.perf_counter()

    mergeTime = end - start

    print(filename)
    print('Python Sort:', pythonTime)
    print('Selection Sort:', selectionTime)
    print('Merge Sort:', mergeTime)

def main():
    test('list5k.txt')
    print()
    test('list50k.txt')
    print()
    test('list100k.txt')

main()