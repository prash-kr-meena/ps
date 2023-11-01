"""
Bubble Sort Algorithm
Given an array of size n, sort it in ascending order

The Idea is

for the current unsorted array  arr[0, n)
If we keep swapping 2 adjacent elements, such that the larger element is on the right and smaller element is on the left
then when we reach to the end of the array, the largest element of the array will be at the last position
ie the largest element is now at its correct position

now we can repeat the same process for the remaining unsorted array arr[0,n-1)
After (N-1) iterations , we get a sorted array.

NOTE :  Unlike selection sort, here, sorting is done from the back

TUF: https://takeuforward.org/data-structure/bubble-sort-algorithm/                 See the diagram
"""
from typing import List

from Utils.Array import swap_array_elements


def bubble_sort(arr: List[int]) -> None:
    """
    Time  : O(n^2)
    Space : O(1)
    :param arr: Array of integers
    """
    n = len(arr)
    for iteration in range(0, n):  # n-1 iteration
        for i in range(0, (n - 1) - iteration):
            if arr[i] > arr[(i + 1)]:
                swap_array_elements(arr, i, i + 1)


if __name__ == '__main__':
    lot_of_numbers = [
        [10, 5, 10, 15, 10, 5, -1, -2, -3, -4, -5],
        [6, 5, 4, 3, 3, 2, 3, 3, -2, -3, -4, -5, 3, 3, 1, 1, 9, 9, 7, 6],
        [2, 2, 3, -2, -3, -4, -5, 4, 4, 2],
        [10, 5, 10, 15, -2, -3, -4, -510, 5, 34, 45, 56, ]
    ]
    for numbers in lot_of_numbers:
        print("Unsorted :", numbers)
        bubble_sort(numbers)
        print("Sorted   :", numbers)
        print()
