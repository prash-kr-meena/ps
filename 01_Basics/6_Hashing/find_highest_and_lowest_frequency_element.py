"""
Find the highest/lowest frequency element

Article
TUF :
GFG :   https://www.geeksforgeeks.org/difference-between-highest-and-least-frequencies-in-an-array/
"""
import math
from typing import List, Tuple, Dict


# Difference between highest and least frequencies in an array
def find_highest_and_lowest_frequency_element(nums: List[int]) -> Tuple[int, int, int, Dict[int, int]]:
    # return (max_freq, min_freq, diff , frequency_map)
    """
    Time  : O(n)
    Space : O(n)
    Note  : This approach works with element which both -ve and +ve elements
    """
    freq_map = {}
    max_freq_till_now = -math.inf
    min_freq_till_now = math.inf
    for num in nums:
        last_freq = freq_map.get(num, 0)
        curr_freq = last_freq + 1
        freq_map[num] = curr_freq

        max_freq_till_now = max(max_freq_till_now, curr_freq)
        min_freq_till_now = min(min_freq_till_now, curr_freq)

    diff = max_freq_till_now - min_freq_till_now
    return max_freq_till_now, min_freq_till_now, diff, freq_map


if __name__ == '__main__':
    lot_of_numbers = [
        [10, 5, 10, 15, 10, 5],
        [10, 5, 10, 15, 10, 5, 1, 2, 3, 4, 5, 6, 5, 4, 3, 3, 2, 3, 3, 3, 3, 1, 1, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 7, 6],
        [2, 2, 3, 4, 4, 2],
        [10, 5, 10, 15, 10, 5, 34, 45, 56, 34, 45, 6, 73, 43, 46, 57, 67, 8]
    ]
    for numbers in lot_of_numbers:
        print(find_highest_and_lowest_frequency_element(numbers))
