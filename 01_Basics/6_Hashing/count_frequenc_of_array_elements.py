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
TUF : https://takeuforward.org/data-structure/count-frequency-of-each-element-in-the-array/
GFG : https://www.geeksforgeeks.org/count-frequencies-elements-array-o1-extra-space-time/
        Note :  This problem can be solved in Constant space as well, checkout last solution on GFG article
                It involves a little mathematics,
                but it also has a constraint that the number are +ve only and  strictly present from 0 to n

                Below is a video explanation of the same, it is not that great though
                Chances are slim that somebody will ask this question,
                just know it is possible when data is present with such restriction
        Youtube : https://youtu.be/UW1InjlrXFU?t=135

Practice

"""
from typing import List, Dict
from collections import defaultdict


def count_frequency_of_array_elements(nums: List[int]) -> Dict[int, int]:
    """
    Time  : O(n)
    Space : O(n)
    Note  : This approach works with element which both -ve and +ve elements
    """
    freq_map = {}
    for num in nums:
        last_freq = freq_map.get(num, 0)  # if not present give back 1
        freq_map[num] = last_freq + 1

    return freq_map


def count_frequency_of_array_elements_via_default_dictionary(numbers) -> defaultdict:
    ddict = defaultdict(lambda: 0)  # ie if key not found return 0
    # ddict = defaultdict(int)  # int function by default produces 0
    for num in numbers:
        ddict[num] = ddict[num] + 1
    return ddict


if __name__ == '__main__':
    lot_of_numbers = [
        [10, 5, 10, 15, 10, 5],
        [2, 2, 3, 4, 4, 2],
        [10, 5, 10, 15, 10, 5, 34, 45, 56, 34, 45, 6, 73, 43, 46, 57, 67, 8],
        [10, 5, 10, 15, 10, 5, 1, 2, 3, 4, 5, 6, 5, 4, 3, 3, 2, 3, 3, 3, 3, 1, 1, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 7, 6]
    ]
    for numbers in lot_of_numbers:
        print(count_frequency_of_array_elements(numbers))
        print(count_frequency_of_array_elements_via_default_dictionary(numbers).items())
