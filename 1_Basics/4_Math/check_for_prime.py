"""
Check if a number is prime or not

Problem Statement:  Given a number, check whether it is prime or not.
                    A prime number is a natural number that is only divisible by 1 and by itself.




Note :  0 and 1 Both are not prime numbers              Important Fact

        Natural Number = [1, inf)
        Whole Number   = [0, inf)

        Whole numbers include all the natural numbers along with zero.

        Zero is neither prime nor composite. Since any number times zero equals zero,
        there are an infinite number of factors for a product of zero.

        Using this definition, 1 can be divided by 1 and the number itself, which is also 1, so 1 is a prime number.
        However, modern mathematicians define a number as prime if it is divided by exactly two numbers.


Examples 1 2 3 5 7 11 13 17 19 ...

    Input: N = 3
    Output: Prime
    Explanation: 3 is a prime number

    Input: N = 26
    Output: Non-Prime
    Explanation: 26 is not prime
"""
import math


def is_prime(num: int) -> bool:
    if num == 0 or num == 1:
        return False

    for divisor in range(2, int(math.sqrt(num)) + 1):  # [2, sqrt(num)]     Both Inclusive
        if num % divisor == 0:
            return False
    return True  # If not returned already


if __name__ == '__main__':
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 23, 27, 29, 31, 37, 97, 123, 153,
               370, 179, 1253, 1634]
    for number in numbers:
        print(f"{number:5} \t{is_prime(number)}")
        # print(f"{number} \t{all_divisors_optimized(number)}")
        # print()
