from bisect import bisect_left
from typing import List


def binary_search_iterative(a, x):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if a[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif a[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


def binary_search_recursive(a, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if a[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif a[mid] > x:
            return binary_search_recursive(a, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search_recursive(a, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


def binary_search_bisect_left(a: List[int], x: int):
    i = bisect_left(a, x)
    #
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1
