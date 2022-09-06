"""


Approaches :
1. Sorting
2. Quick Selection
3. Heap             ->   Implemented in teh Heap package
"""
from typing import List


def find_kth_smallest__via_sorting(nums: List[int]) -> int:
    pass


def find_kth_smallest__via_quick_select(nums: List[int]) -> int:
    pass


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
        print("Sorting      : ", find_kth_smallest__via_sorting(numbers))
        print("Quick Select : ", find_kth_smallest__via_quick_select(numbers))
        print()
