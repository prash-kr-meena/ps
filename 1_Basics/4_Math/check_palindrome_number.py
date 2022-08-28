"""
TUF https://takeuforward.org/data-structure/check-if-a-number-is-palindrome-or-not/
GFG https://www.geeksforgeeks.org/check-if-a-number-is-palindrome/
GFG https://www.geeksforgeeks.org/check-number-palindrome-not-without-using-extra-space/

Check if a number is Palindrome or Not
Problem Statement:  Given a number check if it is a palindrome.


Variations:
* Do it with space and without space
* The number is huge that it can't be fit into long
    Note :  This does not apply to python, but in case asked what we can do is
            we can convert it to string and then do a palindrome check

Accepted
* Leetcode : https://leetcode.com/problems/palindrome-number/
"""
from reverse_a_number import reverse_positive_number


def check_palindrome_number(num: int) -> bool:
    """
    from the last problem we know how to reverse a number
    so if reversed_number == number
        then it's a palindrome

    Time & Space : Same as reverse_number() method
    as no other significant operation is being done
    """
    num = abs(num)  # Edge case to handle negative numbers, otherwise -ve sing will also be part of the number
    reversed_num = reverse_positive_number(num)
    return num == reversed_num


def check_palindrome_number__using_string(num: int) -> int:
    num = abs(num)  # Edge case to handle negative numbers, otherwise -ve sing will also be part of the number
    num_str = str(num)

    i, j = 0, len(num_str) - 1
    while i <= j:
        if num_str[i] != num_str[j]:
            return False
        i += 1
        j -= 1

    return True  # Traversal Completed, and No mismatch found


def check_palindrome_number__without_space(num: int) -> bool:
    """
    GFG https://www.geeksforgeeks.org/check-number-palindrome-not-without-using-extra-space/

    Okay Question, not that hard but not much important just give it a read
    """

    pass


if __name__ == '__main__':
    numbers = [-232, -344, -1, 0, 1, 10, 202, 98765432100000000000000000123456789]
    for number in numbers:
        print(
            f"%40d \t%s \t%s \t%s" % (number,
                                      check_palindrome_number(number),
                                      check_palindrome_number__using_string(number),
                                      check_palindrome_number__without_space(number)
                                      )
        )
