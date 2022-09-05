"""
Selection Sort Algorithm

Given an array of size n, sort it in ascending order

The Idea is to
* Find the minimum element in the unsorted array  arr[0,n) and
  swap it with the element at the beginning.
* Do the exact same on the remaining unsorted array arr[1,n)

Article
TUF : https://takeuforward.org/sorting/selection-sort-algorithm/        See the Visualization
"""
from typing import List

from Utils.Array import swap_array_elements


def selection_sort(arr: List[int]) -> None:
    """
    Time  : O(n^2)
    Space : O(1)
    :param arr: Array of integers
    """
    n = len(arr)
    for i in range(0, n):  # [0, n)
        index_of_smallest_element = i
        for j in range(i, n):  # [i, n)     # loop to find the smallest in the unsorted array [i, n)
            if arr[j] < arr[index_of_smallest_element]:
                index_of_smallest_element = j

        # after finding the smallest number's index, do the swap
        swap_array_elements(arr, i, index_of_smallest_element)


if __name__ == '__main__':
    lot_of_numbers = [
        [10, 5, 10, 15, 10, 5, -1, -2, -3, -4, -5],
        [6, 5, 4, 3, 3, 2, 3, 3, -2, -3, -4, -5, 3, 3, 1, 1, 9, 9, 7, 6],
        [2, 2, 3, -2, -3, -4, -5, 4, 4, 2],
        [10, 5, 10, 15, -2, -3, -4, -510, 5, 34, 45, 56, ]
    ]
    for numbers in lot_of_numbers:
        print("Unsorted :", numbers)
        selection_sort(numbers)
        print("Sorted   :", numbers)
        print()
