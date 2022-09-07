"""


Approaches :
1. Sorting
2. Quick Selection
3. Heap             ->   Implemented in teh Heap package


Assumption : The kth element is bing counted from 1 and not 0
                hence we would return the arr[k-1]th element instead of arr[k]

Corner Case:    The same duplicity case applies here as well
"""
import random
from typing import List


def find_kth_smallest__via_sorting(nums: List[int], k: int) -> int:
    """
    Time  : O(n lg n)
    Space : O(1)            # I know I am using O(n) space, but that will not be the real world solution
    """
    sorted_nums = sorted(nums)  # Note : It should have been   nums.sort()  ie inplace sorting
    # But in my as I have the same input for the next method, I would not want to change its actual input

    return sorted_nums[k - 1]


def find_kth_smallest__via_quick_select(nums: List[int], k: int) -> int:
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
        kth = random.randint(1, len(numbers))  # [1, n-1]  Both included       The kth element is bing counted from 1
        print("kth : ", kth)
        print("Original Sequence    : ", numbers)
        print("Sorted Sequence      : ", sorted(numbers))
        print("kth by Sorting       : ", find_kth_smallest__via_sorting(numbers, kth))
        print("kth by Quick Select  : ", find_kth_smallest__via_quick_select(numbers, kth))
        print()
