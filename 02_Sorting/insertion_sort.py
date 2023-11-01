"""
Insertion Sort Algorithm

Remember The Playing Card

Youtube : https://www.youtube.com/watch?v=7kIVfVY6Axk          [first 10 minutes only]  Greatly Explained - Love Babar
TUF     : https://takeuforward.org/data-structure/insertion-sort-algorithm/
"""
from typing import List

from Utils.Array import swap_array_elements


def insertion_sort(arr: List[int]) -> None:
    """
    Time  : O(n^2)
    Space : O(1)
    :param arr: Array of integers
    """
    n = len(arr)
    for i in range(1, n):
        j = i  # j is temp variable to traverse back and shift element to correct  position
        while j != 0 and arr[j] < arr[j - 1]:
            swap_array_elements(arr, j, j - 1)
            j = j - 1  # going back


if __name__ == '__main__':
    lot_of_numbers = [
        [10, 5, 10, 15, 10, 5, -1, -2, -3, -4, -5],
        [6, 5, 4, 3, 3, 2, 3, 3, -2, -3, -4, -5, 3, 3, 1, 1, 9, 9, 7, 6],
        [2, 2, 3, -2, -3, -4, -5, 4, 4, 2],
        [10, 5, 10, 15, -2, -3, -4, -510, 5, 34, 45, 56, ]
    ]
    for numbers in lot_of_numbers:
        print("Unsorted :", numbers)
        insertion_sort(numbers)
        print("Sorted   :", numbers)
        print()
