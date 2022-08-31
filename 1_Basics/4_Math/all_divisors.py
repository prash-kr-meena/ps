"""
Print all Divisors of a given Number

TUF : https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number/
GFG : https://www.geeksforgeeks.org/sum-divisors-1-n/


Problem Statement: Given a number, print all the divisors of the number. A divisor is a number that gives remainder as zero when divided.

Examples:
    Input: n = 36
    Output: 1 2 3 4 6 9 12 18 36
    Explanation: All the divisors of 36 are printed.

    Input: n = 97
    Output: 1 97
    Explanation: Since 97 is a prime number, only 1 and 97 are printed.

"""
import math
from typing import List


def all_divisors_optimized(num: int) -> List[int]:
    """
    If we take a closer look, we can notice that, the quotient of a division by one of the divisors is actually another divisor.
    Like, 4 divides 36.
    The quotient is 9,  and 9 also divides 36.

    See the image on TUF        For better understanding


    Time    : O(n)
    Space   : O(1)
    """
    divisors = [1]  # 1 divides all the numbers
    for divisor in range(2, int(math.sqrt(num)) + 1):  # sqrt(num) is included
        if num % divisor == 0:
            divisors.append(divisor)
            quotient = number // divisor
            if quotient != divisor:  # To handle duplicates, e.g. in case of 36     6 x 6 is 36
                divisors.append(quotient)
    divisors.append(num)  # every number divides itself
    return divisors


def all_divisors(num: int) -> List[int]:
    """
    Time    : O(n)
    Space   : O(1)
    """
    divisors = []
    for divisor in range(1, num + 1):  # ie num included
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors


if __name__ == '__main__':
    numbers = [0, 3, 9, 10, 36, 97, 123, 153, 370, 179, 1253, 1634]
    for number in numbers:
        print(f"{number} \t{all_divisors(number)}")
        print(f"{number} \t{all_divisors_optimized(number)}")
        print()
