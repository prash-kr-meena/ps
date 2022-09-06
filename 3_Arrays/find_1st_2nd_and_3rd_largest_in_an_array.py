"""
Find 1st 2nd and 3rd Largest elements in an array

Important part could be handling the corner cases, like handling the duplicates (even if you sort it)

Approach 1 : sorting   O(n lg n)
Approach 2 : 1 Pass    O(n)                 The below implementation
"""
import math
from typing import List, Tuple


def find_1st_largest(nums: List[int]) -> int:
    first_max = -math.inf  # -ve Infinity
    for num in nums:
        if num > first_max:
            first_max = num
    return first_max


def find_1st_and_2nd_largest(nums: List[int]) -> Tuple[int, int]:
    first_max = second_max = -math.inf  # -ve Infinity
    for num in nums:
        if num > first_max:
            second_max = first_max
            first_max = num

        elif num > second_max and num != first_max:  # Equality Check : To handle duplicate cases           IMPORTANT
            second_max = num

    return first_max, second_max


def find_1st_2nd_and_3rd_largest(nums: List[int]) -> Tuple[int, int, int]:
    first_max = second_max = third_max = -math.inf  # -ve Infinity
    for num in nums:
        if num > first_max:
            third_max = second_max
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:  # Equality Check : To handle duplicate cases       IMPORTANT
            third_max = second_max
            second_max = num
        elif num > third_max and num != second_max and num != first_max:
            third_max = num

    return first_max, second_max, third_max


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
        print("1st : ", find_1st_largest(numbers))
        print("1st_and_2nd : ", find_1st_and_2nd_largest(numbers))
        print("1st_2nd_and_3rd : ", find_1st_2nd_and_3rd_largest(numbers))
        print()
