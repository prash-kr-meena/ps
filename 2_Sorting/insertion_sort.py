"""
Remember The Playing Card

Youtube : https://www.youtube.com/watch?v=7kIVfVY6Axk                                                       Love Babar
TUF     : https://takeuforward.org/data-structure/insertion-sort-algorithm/
"""
from typing import List


def insertion_sort(arr: List[int]) -> None:
    pass


if __name__ == '__main__':
    lot_of_numbers = [
        [10, 5, 10, 15, 10, 5, -1, -2, -3, -4, -5],
        [6, 5, 4, 3, 3, 2, 3, 3, -2, -3, -4, -5, 3, 3, 1, 1, 9, 9, 7, 6],
        [2, 2, 3, -2, -3, -4, -5, 4, 4, 2],
        [10, 5, 10, 15, -2, -3, -4, -510, 5, 34, 45, 56, ]
    ]
    for numbers in lot_of_numbers:
        print(insertion_sort(numbers))
