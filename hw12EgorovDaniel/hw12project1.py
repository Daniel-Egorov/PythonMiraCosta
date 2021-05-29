"""
{
    "File": "hw12project1.py",
    "Author": "Daniel Egorov",
    "Date": "05/01/21",
    "Desc": [
        "a program to test between linear and binary searches"
    ],
    "Algorithm": [
        "create a function to execute a linear search",
        "create a function to execute a binary search",
        "test them against each other with different sized lists",
        "and different elements of searching to see which is faster"
    ]
}

"""
import time

def linearSearch(array, search):
    for i in range(len(array)):
        if array[i] == search:
            return i
    return -1

def binarySearch(array, search, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if array[mid] == search:
        return mid

    elif array[mid] > search:
        return binarySearch(array, search, low, mid -1)

    elif array[mid] < search:
        return binarySearch(array, search, mid + 1, high)

def testSearches(array, search):
    startTime = time.perf_counter()
    linearSearch(array, search)
    endTime = time.perf_counter()

    print(f'type: linear | size: {len(array) // 1000}k | search: {search} | time:', endTime - startTime)

    startTime = time.perf_counter()
    binarySearch(array, search, 0, len(array) - 1)
    endTime = time.perf_counter()

    print(f'type: binary | size: {len(array) // 1000}k | search: {search} | time:', endTime - startTime)


def main():
    list1k = [x for x in range(1000)]
    list10k = [x for x in range(10000)]
    list100k = [x for x in range(100000)]
    
    testSearches(list1k, 100)
    testSearches(list1k, 500)
    testSearches(list1k, 999)
    testSearches(list10k, 100)
    testSearches(list10k, 5000)
    testSearches(list10k, 9999)
    testSearches(list100k, 100)
    testSearches(list100k, 50000)
    testSearches(list100k, 99999)

main()