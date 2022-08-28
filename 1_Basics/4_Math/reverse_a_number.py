"""
Reverse a number
https://takeuforward.org/c-programs/reverse-a-number-in-c/

Problem Statement: Given a number N reverse the number and print it.
Assuming N is +ve
If its negative we would need to handle -ve numbers as well


Examples:
    Input: N = 123
    Output: 321

    Input: N = -234
    Output: -432

Accepted
* LeetCode : https://leetcode.com/problems/palindrome-number/
"""


def reverse_positive_number(num: int) -> int:
    """
    Given  num > 0
    The idea is to extract digits from end of the given number and create a new number in reverse order.

    Time Complexity : O(n),  Where n is the length of the given number
    Space Complexity: O(1)
    """
    reversed_num = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        reversed_num = (reversed_num * 10) + last_digit
    return reversed_num


def reverse_number__using_string(num: int) -> int:
    """
    Time Complexity : O(1)      If we ignore what the time taken for python to convert integer to string
    Space Complexity: O(1)
    """
    num_string = str(num)
    reversed_num_str = num_string[::-1]
    return int(reversed_num_str)


def reverse_number_including_negative(num: int) -> int:
    was_negative = num < 0  # Handling the -ve sign
    num = abs(num)
    reversed_num = reverse_positive_number(num)
    return -reversed_num if was_negative else reversed_num


def reverse_number_including_negative__using_string(num: int) -> int:
    was_negative = num < 0  # Handling the -ve sign
    num = abs(num)
    reversed_num = reverse_number__using_string(num)
    return -reversed_num if was_negative else reversed_num


if __name__ == '__main__':
    numbers = [-123456789, -3, 0, 321, 123456789]
    for number in numbers:
        print(f"{number:10}     ->"
              f"{reverse_number_including_negative(number) :15}"
              f"{reverse_number_including_negative__using_string(number):15}")
