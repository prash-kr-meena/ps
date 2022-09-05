"""
Count frequency of each element in the array
Problem statement: Given an array, we have found the number of occurrences of each element in the array.

Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
        5   2
        15  1
Explanation:    10 occurs 3 times in the array
                5 occurs 2 times in the array
                15 occurs 1 time in the array


Input: arr[] = {2,2,3,4,4,2};
Output: 2  3
        3  1
        4  2
Explanation:    2 occurs 3 times in the array
                3 occurs 1 time in the array
                4 occurs 2 time in the array

Article


Practice

"""
from typing import List, Dict


def count_frequency_of_array_elements(nums: List[int]) -> Dict[int, int]:
    """
    Time  : O(n)
    Space : O(n)
    """
    freq_map = {}
    for num in nums:
        current_freq = freq_map.get(num, 0)  # if not present give back 1
        freq_map[num] = current_freq + 1

    return freq_map


if __name__ == '__main__':
    lot_of_numbers = [
        [10, 5, 10, 15, 10, 5],
        [2, 2, 3, 4, 4, 2],
        [10, 5, 10, 15, 10, 5, 34, 45, 56, 34, 45, 6, 73, 43, 46, 57, 67, 8],
        [10, 5, 10, 15, 10, 5, 1, 2, 3, 4, 5, 6, 5, 4, 3, 3, 2, 3, 3, 3, 3, 1, 1, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 7, 6]
    ]
    for numbers in lot_of_numbers:
        print(count_frequency_of_array_elements(numbers))
