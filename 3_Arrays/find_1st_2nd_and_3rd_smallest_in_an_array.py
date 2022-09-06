"""
Find 1st 2nd and 3rd Smallest elements in an array

Important part could be handling the corner cases, like handling the duplicates (even if you sort it)

Approach 1 : sorting   O(n lg n)
Approach 2 : 1 Pass    O(n)                 The below implementation


###
You can do a comparison before returning the result, in case you don't find the 2nd or 3rd largest and
you want to do something special at that time

    if second_largest == math.inf:
        print("There was no second smallest")
        return first_largest, None
"""

import math
from typing import List, Tuple


def find_1st_smallest(nums: List[int]) -> int:
    first_min = +math.inf  # +ve Infinity
    for num in nums:
        if num < first_min:
            first_min = num
    return first_min


def find_1st_and_2nd_smallest(nums: List[int]) -> Tuple[int, int]:
    first_min = second_min = +math.inf  # +ve Infinity
    for num in nums:
        if num < first_min:
            second_min = first_min
            first_min = num

        elif num < second_min and num != first_min:  # Equality Check : To handle duplicate cases           IMPORTANT
            second_min = num

    return first_min, second_min


def find_1st_2nd_and_3rd_smallest(nums: List[int]) -> Tuple[int, int, int]:
    first_min = second_min = third_min = +math.inf  # +ve Infinity
    for num in nums:
        if num < first_min:
            third_min = second_min
            second_min = first_min
            first_min = num
        elif num < second_min and num != first_min:  # Equality Check : To handle duplicate cases       IMPORTANT
            third_min = second_min
            second_min = num
        elif num < third_min and num != second_min and num != first_min:
            third_min = num

    return first_min, second_min, third_min


if __name__ == '__main__':
    lot_of_numbers = [
        [10, 5, 10, 15, 10, 5, -1, -2, -3, -4, -5],
        [6, 5, 4, 3, 3, 2, 3, 3, -2, -3, -4, -5, 3, 3, 1, 1, 9, 9, 7, 6],
        [2, 2, 3, -2, -3, -4, -5, 4, 4, 2],
        [10, 5, 10, 15, -2, -3, -4, -510, 5, 34, 45, 56, ],

        [12, 13, 2, 11, 0, 10],
        [1, 2, 3, 4, 5, 6, 7],
        [7, 7, 7, 7, 7, 7, 7],
        [3, 2, 2, 1, 1, 2, 3]
    ]
    for numbers in lot_of_numbers:
        print(numbers)
        print("1st : ", find_1st_smallest(numbers))
        print("1st_and_2nd : ", find_1st_and_2nd_smallest(numbers))
        print("1st_2nd_and_3rd : ", find_1st_2nd_and_3rd_smallest(numbers))
        print()
