"""
Count digits in a number
https://takeuforward.org/data-structure/count-digits-in-a-number/


Problem Statement: Given an integer N , write program to count number of digits in N.

Examples:
    Input: N = 12345
    Output: 5

    Input: N = 8394
    Output: 4



Good Edge Cases
* Negative Number (Here the -ve sign should not be counted)
* Zero
"""
import math


def count_digits(num: int) -> int:
    """
    Time Complexity: O (n) where n is the number of digits in the given integer
    Space Complexity: O(1)
    """
    num = abs(num)  # Edge Cases, to handle negative values

    if num == 0:  # Edge case
        return 1

    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count


def count_digits__using_string(num: int) -> int:
    """
    Time Complexity: O (1)
    Space Complexity: O(1)
    """
    num = abs(num)  # Handling -ve cases
    number_string = str(num)
    return len(number_string)


def count_digits__using_logarithm(num: int) -> int:  # Most Optimized
    """
    Time  : O(1)
    Space : O(1)
    """

    num = abs(num)  # No, you can't take the log of a negative number.
    if num == 0:  # Edge Case: As log of 0 is undefined
        return 1
    return int(math.log10(num)) + 1  # Remember this formula


if __name__ == '__main__':
    numbers = [3, 0, -1, -144, 435345345]
    for number in numbers:
        print(count_digits(number), count_digits__using_string(number), count_digits__using_logarithm(number))
