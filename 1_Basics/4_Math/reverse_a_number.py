"""
Reverse a number
https://takeuforward.org/c-programs/reverse-a-number-in-c/

Problem Statement: Given a number N reverse the number and print it.
Assuming N is +ve
If its negative we would need to handle -ve numbers as well


Examples:
    Input: N = 123
    Output: 321

    Input: N = 234
    Output: 432
"""


def reverse_a_number(num: int) -> int:
    """
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


def reverse_a_number_using_string(num: int) -> int:
    num_string = str(num)
    reversed_num_str = num_string[::-1]
    return int(reversed_num_str)


if __name__ == '__main__':
    numbers = [3, 0, 321, 123456789]
    for number in numbers:
        print(reverse_a_number(number), reverse_a_number_using_string(number))