"""
Armstrong Number
GFG :   https://www.geeksforgeeks.org/program-for-armstrong-numbers/


Problem Statement: Given a number, check if it is Armstrong Number or Not

A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.
    abcd… = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ….


Examples
    Input:153
    Output: Yes, it is an Armstrong Number
    Explanation: 1^3 + 5^3 + 3^3 = 153

    Input:170
    Output: No, it is not an Armstrong Number
    Explanation: 1^3 + 7^3 + 0^3 != 170


Accepted
LC  :   https://leetcode.com/problems/armstrong-number/                         LeetCode Premium
GFG :   https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1
"""

from count_digits import *


def is_armstrong_number(num: int) -> bool:
    """
    a little similar to the count_digit.py problem, as I need to traverse each digit

    Time  : O(n)         O(n) + O(n) = O(2n)     where n is the number of digits
    Space : O(1)
    """
    actual_num_value = num
    number_of_digits = count_digits__using_logarithm(num)
    sum_of_digits = 0

    while num > 0:
        last_digit = num % 10
        num = num // 10
        sum_of_digits += int(math.pow(last_digit, number_of_digits))

    return sum_of_digits == actual_num_value


def is_armstrong_number__using_string(num: int) -> bool:
    """
    Time  : O(n)
    Space : O(1)
    """
    num_str = str(num)
    number_of_digits = len(num_str)

    sum_of_digits = 0
    for digit_char in num_str:
        sum_of_digits += int(digit_char) ** number_of_digits  # power/exponent operator **

    return sum_of_digits == num


if __name__ == '__main__':
    numbers = [0, 3, 9, 10, 123, 153, 370, 179, 1253, 1634]
    for number in numbers:
        print(f"{number:7}    \t{is_armstrong_number(number)}  {'':3} \t{is_armstrong_number__using_string(number)}")
